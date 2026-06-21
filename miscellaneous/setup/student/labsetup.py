#!/usr/bin/env python3

import sys

"""Parse labenv.yaml and set up the student lab environment.

Steps performed:
1. Load non-confidential env vars from labenv.yaml.
2. Install Ollama if absent (idempotent).
3. Create projects/embedding/.venv, pip-compile, pip-sync,
   and register Jupyter kernel if venv absent (idempotent).
4. Install PKM CLI tools (poppler-utils, html2text) if absent
   (idempotent — skipped if both are already on PATH).
5. Generate ~/.ssh/<username>_id_ed25519_server key pair if it does not
   exist (idempotent — skipped if the key is already present).
4. Post the public key to #meetup-notifications so the instructor
   can install it on the Docker server (instructor.md Section 3) —
   only when a new key was generated in step 5 (idempotent).
5. Write ~/.ssh/config entries (Host ai-lab-int and Host ai-lab)
   for the internal/external lab server addresses, replacing any
   prior versions of either block.
6. Validate SSH connectivity to ai-lab-int and ai-lab (either
   succeeding is OK; ai-lab is the off-campus default).
8. Validate that DISCORD_WEBHOOK_URL is set.
9. If `gh auth status` exits 0: generate
   ~/.ssh/<username>_id_ed25519_github if absent, upload the
   public key to GitHub if not already registered (idempotent),
   write Host github.com config entry, and validate GitHub SSH
   authentication. Skipped with WARN if not authenticated — run
   `gh auth login` first (dev_workbench.md).
10. On macOS, materialize .devcontainer/ from
    miscellaneous/tools/VM/devcontainer/ so VSCode's Dev
    Containers prompt fires (miscellaneous/tools/VM/setup.md).
    On Windows/WSL or native Linux, remove .devcontainer/ if
    present — the lab environment is already native there and
    the prompt is redundant. Idempotent.

Steps 2–5 are skipped when labenv.yaml still contains placeholder
values (strings wrapped in < >). DISCORD_WEBHOOK_URL must be set
before running — retrieve it from the #meetup-notifications pinned
message posted by the instructor (instructor.md Section 2).
"""
import getpass
import os
import shutil
import subprocess
import sys
import yaml
import requests
from pathlib import Path

LABENV = Path(__file__).parent / "labenv.yaml"
SECRET_KEY = "DISCORD_WEBHOOK_URL"
SSH_DIR = Path.home() / ".ssh"
SSH_HOST_ALIAS = "ai-lab"
SSH_HOST_ALIAS_INT = "ai-lab-int"

SSH_KEYS = (
  "DOCKER_SERVER_ID_INTERNAL",
  "DOCKER_SERVER_SSH_PORT_INTERNAL",
  "DOCKER_SERVER_ID_EXTERNAL",
  "DOCKER_SERVER_SSH_PORT_EXTERNAL",
  "DOCKER_SERVER_USERNAME",
)

# Use local OS username to name the key so instructors can
# disambiguate public keys from different student laptops.
_USERNAME = getpass.getuser()
SSH_KEY = SSH_DIR / f"{_USERNAME}_id_ed25519_server"
SSH_CONFIG = SSH_DIR / "config"

GITHUB_HOST_ALIAS = "github.com"
GITHUB_SSH_KEY = SSH_DIR / f"{_USERNAME}_id_ed25519_github"


def _load_env() -> dict[str, str]:
  with LABENV.open() as f:
    return {k: str(v) for k, v in yaml.safe_load(f).items()}


def _set_env(env: dict[str, str]) -> None:
  for key, value in env.items():
    os.environ[key] = value
    print(f"  SET  {key}={value}")


def _gh_env() -> dict[str, str]:
  """Environment for `gh` calls, with GH_TOKEN/GITHUB_TOKEN unset.

  A GH_TOKEN exported for unrelated purposes (e.g. a code-review
  PAT) overrides the `gh auth login` session and its
  admin:public_key scope (github.md), breaking SSH key setup.
  """
  env = os.environ.copy()
  env.pop("GH_TOKEN", None)
  env.pop("GITHUB_TOKEN", None)
  return env


def _is_placeholder(value: str) -> bool:
  stripped = value.strip()
  return stripped.startswith("<") and stripped.endswith(">")


def _generate_ssh_key() -> bool:
  """Generate ed25519 key pair if absent; return True if generated."""
  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  if SSH_KEY.exists():
    print(f"  OK   SSH key already exists: {SSH_KEY} (skipping)")
    return False
  subprocess.run(
    [
      "ssh-keygen", "-t", "ed25519",
      "-f", str(SSH_KEY),
      "-N", "",              # no passphrase — lab convenience
      "-C", f"{_USERNAME}@{os.uname().nodename}",
    ],
    check=True,
    capture_output=True,
  )
  print(f"  GEN  SSH key pair created: {SSH_KEY}")
  return True


def _post_pubkey_to_discord(env: dict[str, str]) -> None:
  """Post the student's public key to #meetup-notifications.

  The instructor reads the channel and installs the key into
  the DOCKER_SERVER_USERNAME account on DOCKER_SERVER_ID
  (instructor.md Section 3 — Add each student's SSH public key).
  """
  webhook = os.environ.get(SECRET_KEY)
  if not webhook:
    print(
      f"  SKIP public-key post — {SECRET_KEY} not set.\n"
      "  Set it and re-run so the instructor can install your key."
    )
    return

  pubkey = SSH_KEY.with_suffix(".pub").read_text().strip()
  server = env.get("DOCKER_SERVER_ID_INTERNAL", "<server>")
  user = env.get("DOCKER_SERVER_USERNAME", "<user>")

  msg = (
    f"🔑 **SSH public key** from student `{_USERNAME}` "
    f"(laptop: `{os.uname().nodename}`)\n"
    f"Please install on `{server}` account `{user}`:\n"
    f"```\n{pubkey}\n```\n"
    "_(instructor.md Section 3 → Add each student's SSH public key)_"
  )
  r = requests.post(webhook, json={"content": msg})
  if r.status_code == 204:
    print(
      f"  POST public key → #meetup-notifications\n"
      "  Ask your instructor to install it, then re-run to "
      "validate SSH."
    )
  else:
    print(
      f"  WARN public-key post failed (HTTP {r.status_code}) — "
      "share your key with the instructor manually.",
      file=sys.stderr,
    )


def _write_ssh_config(env: dict[str, str]) -> None:
  """Write or refresh the ai-lab-int/ai-lab Host blocks.

  Replaces any existing Host ai-lab-int / Host ai-lab blocks in
  ~/.ssh/config with fresh entries for the internal LAN and
  external WAN addresses — re-running after a labenv.yaml change
  keeps both correct instead of preserving stale blocks.
  """
  existing = SSH_CONFIG.read_text() if SSH_CONFIG.exists() else ""

  # Drop any existing "Host ai-lab-int" / "Host ai-lab" blocks
  # (header line plus the indented option lines that follow).
  headers = {f"Host {SSH_HOST_ALIAS_INT}", f"Host {SSH_HOST_ALIAS}"}
  kept = []
  skipping = False
  for line in existing.splitlines():
    if line.strip() in headers:
      skipping = True
      continue
    if skipping and line[:1] in (" ", "\t"):
      continue
    skipping = False
    kept.append(line)

  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  targets = (
    (SSH_HOST_ALIAS_INT, "DOCKER_SERVER_ID_INTERNAL",
     "DOCKER_SERVER_SSH_PORT_INTERNAL"),
    (SSH_HOST_ALIAS, "DOCKER_SERVER_ID_EXTERNAL",
     "DOCKER_SERVER_SSH_PORT_EXTERNAL"),
  )
  entries = "".join(
    f"Host {alias}\n"
    f"  HostName {env[host_key]}\n"
    f"  User     {env['DOCKER_SERVER_USERNAME']}\n"
    f"  Port     {env[port_key]}\n"
    f"  IdentityFile {SSH_KEY}\n"
    for alias, host_key, port_key in targets
  )
  body = "\n".join(kept).rstrip("\n")
  text = (body + "\n\n" if body else "") + entries
  if text == existing:
    print(
      f"  OK   ~/.ssh/config Host {SSH_HOST_ALIAS_INT}, "
      f"Host {SSH_HOST_ALIAS} up to date (skipping)"
    )
    return
  SSH_CONFIG.write_text(text)
  SSH_CONFIG.chmod(0o600)
  print(
    f"  WROTE ~/.ssh/config: Host {SSH_HOST_ALIAS_INT}, "
    f"Host {SSH_HOST_ALIAS}"
  )


def _validate_ssh() -> None:
  reachable = []
  last_stderr = ""
  for alias in (SSH_HOST_ALIAS_INT, SSH_HOST_ALIAS):
    result = subprocess.run(
      [
        "ssh", "-o", "BatchMode=yes",
        "-o", "ConnectTimeout=10",
        alias, "echo", "ok",
      ],
      capture_output=True,
      text=True,
    )
    if result.returncode == 0 and result.stdout.strip() == "ok":
      print(f"  OK   SSH {alias} → connection verified")
      reachable.append(alias)
    else:
      last_stderr = result.stderr.strip()

  if not reachable:
    print(
      f"\n  WARN SSH to {SSH_HOST_ALIAS_INT!r} and "
      f"{SSH_HOST_ALIAS!r} not yet available.\n"
      "  Your public key was posted to #meetup-notifications.\n"
      "  Once the instructor confirms it is installed, re-run "
      "this script to validate the connection. Use "
      f"{SSH_HOST_ALIAS_INT!r} on the lab LAN, or "
      f"{SSH_HOST_ALIAS!r} (default) from off-campus.\n"
      f"  (stderr: {last_stderr!r})"
    )


def _generate_github_ssh_key(github_username: str) -> bool:
  """Generate GitHub SSH key pair if absent; return True if
  generated.
  """
  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  if GITHUB_SSH_KEY.exists():
    print(
      f"  OK   GitHub SSH key exists: {GITHUB_SSH_KEY} (skipping)"
    )
    return False
  subprocess.run(
    [
      "ssh-keygen", "-t", "ed25519",
      "-f", str(GITHUB_SSH_KEY),
      "-N", "",
      "-C", f"{github_username}@github",
    ],
    check=True,
    capture_output=True,
  )
  print(f"  GEN  GitHub SSH key created: {GITHUB_SSH_KEY}")
  return True


def _upload_github_ssh_key(github_username: str) -> None:
  """Upload the GitHub public key if not already registered.

  Checked independently of key generation (via `gh ssh-key list`)
  so a re-run retries the upload even if a prior upload attempt
  failed after the local key was already created. `gh ssh-key`
  requires the `admin:public_key` auth scope — WARN (don't crash)
  if list/add fails, since `gh auth login`'s default scopes omit it.
  """
  title = f"{_USERNAME}-lab-key"
  list_result = subprocess.run(
    ["gh", "ssh-key", "list"],
    capture_output=True, text=True, env=_gh_env(),
  )
  if list_result.returncode == 0 and title in list_result.stdout:
    print(f"  OK   GitHub key '{title}' already uploaded (skipping)")
    return
  add_result = subprocess.run(
    [
      "gh", "ssh-key", "add",
      str(GITHUB_SSH_KEY.with_suffix(".pub")),
      "--title", title,
    ],
    capture_output=True, text=True, env=_gh_env(),
  )
  if add_result.returncode == 0:
    if "already exists" in add_result.stderr:
      print(f"  OK   GitHub key '{title}' already uploaded (skipping)")
    else:
      print(f"  POST GitHub public key uploaded for {github_username}")
  else:
    print(
      "  WARN GitHub key upload failed — grant the scope and "
      "re-run:\n"
      "  gh auth refresh -h github.com -s admin:public_key\n"
      f"  (stderr: {add_result.stderr.strip()!r})",
      file=sys.stderr,
    )


def _write_github_ssh_config() -> None:
  """Append Host github.com block to ~/.ssh/config.

  Idempotent — skipped if the entry already exists.
  """
  existing = SSH_CONFIG.read_text() if SSH_CONFIG.exists() else ""
  for line in existing.splitlines():
    if line.strip() == f"Host {GITHUB_HOST_ALIAS}":
      print(
        f"  OK   ~/.ssh/config entry exists: "
        f"Host {GITHUB_HOST_ALIAS} (skipping)"
      )
      return
  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  entry = (
    f"\nHost {GITHUB_HOST_ALIAS}\n"
    f"  HostName     github.com\n"
    f"  User         git\n"
    f"  IdentityFile {GITHUB_SSH_KEY}\n"
  )
  with SSH_CONFIG.open("a") as f:
    f.write(entry)
  SSH_CONFIG.chmod(0o600)
  print(f"  WROTE ~/.ssh/config entry: Host {GITHUB_HOST_ALIAS}")


def _validate_github_ssh() -> None:
  """Warn (not exit) if GitHub SSH authentication fails.

  GitHub exits 1 even on success — check the stderr message instead.
  """
  result = subprocess.run(
    [
      "ssh", "-o", "BatchMode=yes",
      "-o", "ConnectTimeout=10",
      "git@github.com",
    ],
    capture_output=True,
    text=True,
  )
  if "successfully authenticated" in result.stderr:
    print("  OK   GitHub SSH authentication verified")
  else:
    print(
      "  WARN GitHub SSH not verified.\n"
      "  Ensure your key was uploaded: gh ssh-key list\n"
      f"  (stderr: {result.stderr.strip()!r})",
      file=sys.stderr,
    )


def _validate_secret() -> None:
  if not os.environ.get(SECRET_KEY):
    print(
      f"\nERROR: {SECRET_KEY} is not set.\n"
      "Retrieve it from the pinned message in "
      "#meetup-notifications and run:\n"
      f"  export {SECRET_KEY}=<webhook-url>\n"
      "Never add this value to any committed file.",
      file=sys.stderr,
    )
    sys.exit(1)
  print(f"  OK   {SECRET_KEY} is set (value hidden)")


_EMBEDDING_DIR = (
  Path(__file__).parent.parent / "embedding"
)
_EMBEDDING_VENV = _EMBEDDING_DIR / ".venv"

_SPEED_READING_DIR = (
  Path(__file__).parent.parent
  / "llm_wiki" / "speed-reading"
)
_PIPER_VENV = _SPEED_READING_DIR / ".venv"


def _install_ollama() -> None:
  """Install Ollama via the official install script if absent.

  Required by the AI Local session for running open-weight LLMs
  (Llama, Gemma) locally. Idempotent — skips when ollama is
  already on PATH.
  """
  if shutil.which("ollama"):
    print("  OK   ollama already installed (skipping)")
    return
  print("  INST installing ollama via official script...")
  try:
    subprocess.run(
      ["bash", "-c",
       "curl -fsSL https://ollama.com/install.sh | sh"],
      check=True,
    )
    print("  OK   ollama installed")
  except subprocess.CalledProcessError:
    print(
      "  WARN ollama install failed — install manually:\n"
      "       curl -fsSL https://ollama.com/install.sh | sh",
      file=sys.stderr,
    )


def _setup_embedding_venv() -> None:
  """Create the embedding Python venv and install dependencies.

  Required by the Embeddings Visualization session. Creates
  projects/embedding/.venv, runs pip-compile + pip-sync, and
  registers the Jupyter kernel. Idempotent — skips when the
  venv Python binary already exists.
  """
  venv_py = _EMBEDDING_VENV / "bin" / "python3"
  if venv_py.exists():
    print("  OK   embedding venv already exists (skipping)")
    return
  print("  VENV creating projects/embedding/.venv …")
  subprocess.run(
    ["python3", "-m", "venv", str(_EMBEDDING_VENV)],
    check=True,
  )
  pip = str(_EMBEDDING_VENV / "bin" / "pip")
  subprocess.run([pip, "install", "pip-tools"], check=True)
  subprocess.run(
    [str(_EMBEDDING_VENV / "bin" / "pip-compile"),
     "requirements.in"],
    check=True,
    cwd=str(_EMBEDDING_DIR),
  )
  subprocess.run(
    [str(_EMBEDDING_VENV / "bin" / "pip-sync"),
     "requirements.txt"],
    check=True,
    cwd=str(_EMBEDDING_DIR),
  )
  subprocess.run(
    [
      str(venv_py), "-m", "ipykernel", "install",
      "--user", "--name", ".venv",
      "--display-name", "Python3 (.venv)",
    ],
    check=True,
  )
  print("  OK   embedding venv ready")


def _setup_piper_venv() -> None:
  """Create the speed-reading venv for piper.py if absent.

  Required by the Speed Reading Mindmap session (src/piper.py).
  All pipeline deps are stdlib; the venv is created for
  environment isolation and future extensibility. Idempotent —
  skips when the venv Python binary already exists.
  """
  venv_py = _PIPER_VENV / "bin" / "python3"
  if venv_py.exists():
    print(
      "  OK   speed-reading venv already exists (skipping)"
    )
    return
  print("  VENV creating projects/llm_wiki/speed-reading/.venv")
  subprocess.run(
    ["python3", "-m", "venv", str(_PIPER_VENV)],
    check=True,
  )
  print("  OK   speed-reading venv ready")


_PKM_PACKAGES = {
  "pdftotext": "poppler-utils",
  "html2text": "html2text",
  "zstd": "zstd",
}


def _install_pkm_tools() -> None:
  """Install poppler-utils, html2text, and zstd if not on PATH.

  Required by the Speed Reading Mindmap pipeline (src/piper.py):
  pdftotext converts PDFs; html2text converts HTML pages to plain
  text. zstd is required by the ollama install script to extract
  its release archive. Idempotent — skips the apt call when all
  three CLIs are already present.
  """
  missing = [
    pkg for tool, pkg in _PKM_PACKAGES.items()
    if not shutil.which(tool)
  ]
  if not missing:
    print(
      "  OK   pdftotext, html2text, and zstd already installed "
      "(skipping)"
    )
    return
  print(f"  APT  installing: {', '.join(missing)}")
  subprocess.run(
    ["sudo", "apt", "install", "-y", *missing],
    check=True,
  )
  print("  OK   PKM CLI tools installed")


def _sudo_precheck() -> bool:
  """Authenticate sudo credentials upfront.

  Runs sudo -v to prompt for password once before any apt-install
  steps so subsequent sudo calls succeed without re-prompting.
  Returns True if sudo is available; False if unavailable (e.g.,
  passwordless sudo not configured — apt steps are skipped with
  manual-install instructions).
  """
  print(
    "  SUDO this script installs system packages via sudo.\n"
    "       Enter your password if prompted."
  )
  result = subprocess.run(["sudo", "-v"])
  if result.returncode != 0:
    print(
      "  WARN sudo unavailable — package installs will be skipped.\n"
      "  Install manually: "
      "sudo apt install poppler-utils html2text",
      file=sys.stderr,
    )
    return False
  return True


_DEVCONTAINER_SRC = (
  Path(__file__).parent.parent / "tools" / "VM" / "devcontainer"
)
_DEVCONTAINER_DST = Path(__file__).parent.parent / ".devcontainer"


def _setup_devcontainer() -> None:
  """Materialize .devcontainer/ on macOS only; remove it elsewhere.

  VSCode's "Create/Reopen in Container" prompt fires purely on
  .devcontainer/devcontainer.json's presence
  (miscellaneous/tools/VM/setup.md) — on Windows/WSL or native
  Linux the lab environment is already native, so the container
  is redundant and the prompt is noise.
  Idempotent in both directions.
  """
  if os.uname().sysname == "Darwin":
    _DEVCONTAINER_DST.mkdir(exist_ok=True)
    for name in ("Dockerfile", "devcontainer.json"):
      shutil.copy(_DEVCONTAINER_SRC / name, _DEVCONTAINER_DST / name)
    print("  OK   .devcontainer/ materialized (macOS)")
  elif _DEVCONTAINER_DST.exists():
    shutil.rmtree(_DEVCONTAINER_DST)
    print("  OK   .devcontainer/ removed (not macOS)")
  else:
    print("  OK   .devcontainer/ absent (not macOS, skipping)")


def _ensure_gh_installed() -> bool:
  """Install the GitHub CLI (gh) via apt if not already on PATH.

  Returns True if gh is available afterward, False if absent and
  the apt install failed or was unavailable.
  """
  if shutil.which("gh"):
    return True
  print("  APT  installing: gh")
  try:
    subprocess.run(["sudo", "apt", "install", "-y", "gh"], check=True)
    print("  OK   gh installed")
    return True
  except subprocess.CalledProcessError:
    print(
      "  WARN gh install failed — install manually: "
      "https://cli.github.com",
      file=sys.stderr,
    )
    return False


def main() -> None:
  env = _load_env()
  _set_env(env)
  sudo_ok = _sudo_precheck()
  if sudo_ok:
    _install_pkm_tools()  # installs zstd — required by ollama installer
    _install_ollama()
  _setup_embedding_venv()  # pure Python venv — no sudo needed
  _setup_piper_venv()     # speed-reading venv — no sudo needed
  _setup_devcontainer()   # macOS only — no sudo needed

  ssh_real = all(
    k in env and not _is_placeholder(env[k]) for k in SSH_KEYS
  )

  if ssh_real:
    if _generate_ssh_key():
      _post_pubkey_to_discord(env)
    else:
      print(
        "  SKIP Discord post — key already shared with instructor"
      )
    _write_ssh_config(env)
    _validate_ssh()
  else:
    print(
      "  SKIP SSH setup — labenv.yaml still has placeholder values.\n"
      "  Fill in DOCKER_SERVER_ID_INTERNAL/_EXTERNAL,\n"
      "  DOCKER_SERVER_SSH_PORT_INTERNAL/_EXTERNAL, and\n"
      "  DOCKER_SERVER_USERNAME with real values, then re-run."
    )

  _validate_secret()

  gh_ready = _ensure_gh_installed() and subprocess.run(
    ["gh", "auth", "status"], capture_output=True, env=_gh_env(),
  ).returncode == 0

  if gh_ready:
    github_username = subprocess.run(
      ["gh", "api", "user", "--jq", ".login"],
      capture_output=True, text=True, env=_gh_env(),
    ).stdout.strip()
    _generate_github_ssh_key(github_username)
    _upload_github_ssh_key(github_username)
    _write_github_ssh_config()
    _validate_github_ssh()
  else:
    print(
      "  WARN GitHub CLI not authenticated — skipping GitHub SSH.\n"
      "  Run: gh auth login\n"
      "  See: miscellaneous/tools/dev_workbench/"
      "github_and_git.md#account-setup",
      file=sys.stderr,
    )

  print("\nEnvironment ready.")


if __name__ == "__main__":
  sys.exit(main())
