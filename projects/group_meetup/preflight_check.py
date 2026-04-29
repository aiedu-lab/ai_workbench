#!/usr/bin/env python3
"""Instructor preflight check to validate environment
before starting the lab.

Checks for:
- Python 3.10+
- git, gh, and claude CLIs in PATH
- requests and pyyaml packages installed
- Non-confidential vars present in labenv.yaml with real values
- DISCORD_WEBHOOK_URL set in the shell environment (secret)
- SSH key exists at ~/.ssh/<username>_id_ed25519
- SSH connectivity to the lab server (Host ai-lab in ~/.ssh/config)
- gh CLI installed and authenticated (gh auth status)
- GitHub SSH key exists at ~/.ssh/<username>_id_ed25519_github
- GitHub SSH authentication (ssh git@github.com)
- git global user.name and user.email configured

Non-confidential vars (DISCORD_SERVER, DOCKER_SERVER_*) are read
directly from labenv.yaml so this script works without requiring
labsetup.py to have been run in the same shell session.

Prints PASS or FAIL per item. Always runs all checks.
"""
import getpass
import importlib
import os
import subprocess
import sys
import yaml
from pathlib import Path

LABENV = Path(__file__).parent / "labenv.yaml"
SSH_KEY = Path.home() / ".ssh" / f"{getpass.getuser()}_id_ed25519"
GITHUB_SSH_KEY = (
  Path.home() / ".ssh" / f"{getpass.getuser()}_id_ed25519_github"
)

NON_SECRET_VARS = (
  "DISCORD_SERVER",
  "DOCKER_SERVER_ID",
  "DOCKER_SERVER_USERNAME",
  "DOCKER_SERVER_SSH_PORT",
)


def _labenv() -> dict[str, str]:
  try:
    with LABENV.open() as f:
      return {k: str(v) for k, v in yaml.safe_load(f).items()}
  except Exception as e:
    return {"_error": str(e)}


def _is_placeholder(value: str) -> bool:
  stripped = value.strip()
  return stripped.startswith("<") and stripped.endswith(">")


def check(label, fn):
  try:
    fn()
    print(f"PASS  {label}")
  except Exception as e:
    print(f"FAIL  {label} — {e}")


def cmd_exists(name):
  result = subprocess.run(["which", name], capture_output=True)
  if result.returncode != 0:
    raise RuntimeError(f"{name} not found in PATH")


def pkg_exists(name):
  importlib.import_module(name)


def check_python():
  if sys.version_info < (3, 10):
    raise RuntimeError(
      f"need 3.10+, got "
      f"{sys.version_info.major}.{sys.version_info.minor}"
    )


def check_labenv_var(env: dict[str, str], var: str):
  if "_error" in env:
    raise RuntimeError(f"cannot read labenv.yaml — {env['_error']}")
  if var not in env:
    raise RuntimeError(f"{var} missing from labenv.yaml")
  if _is_placeholder(env[var]):
    raise RuntimeError(
      f"{var} is still a placeholder — update labenv.yaml"
    )


def check_discord_webhook():
  if not os.environ.get("DISCORD_WEBHOOK_URL"):
    raise RuntimeError("DISCORD_WEBHOOK_URL not set in environment")


def check_ssh_key():
  if not SSH_KEY.exists():
    raise RuntimeError(
      f"{SSH_KEY} not found — run labsetup.py to generate it"
    )


def check_ssh():
  result = subprocess.run(
    [
      "ssh", "-o", "BatchMode=yes",
      "-o", "ConnectTimeout=10",
      "ai-lab", "echo", "ok",
    ],
    capture_output=True,
    text=True,
  )
  if result.returncode != 0 or result.stdout.strip() != "ok":
    raise RuntimeError(
      "SSH to ai-lab failed — run labsetup.py, then ask the "
      "instructor to install your public key on the server "
      f"(stderr: {result.stderr.strip()!r})"
    )


def check_gh_install():
  result = subprocess.run(
    ["gh", "--version"], capture_output=True
  )
  if result.returncode != 0:
    raise RuntimeError(
      "gh not runnable — install via: sudo apt install gh"
    )


def check_gh_auth():
  result = subprocess.run(
    ["gh", "auth", "status"], capture_output=True
  )
  if result.returncode != 0:
    raise RuntimeError(
      "gh not authenticated — run: gh auth login\n"
      "  See: tools/dev_workbench/github.md#account-setup"
    )


def check_github_ssh_key():
  if not GITHUB_SSH_KEY.exists():
    raise RuntimeError(
      f"{GITHUB_SSH_KEY} not found — run labsetup.py to generate it"
    )


def check_github_ssh():
  result = subprocess.run(
    [
      "ssh", "-o", "BatchMode=yes",
      "-o", "ConnectTimeout=10",
      "git@github.com",
    ],
    capture_output=True,
    text=True,
  )
  # GitHub always exits 1 even on success; check stderr message
  if "successfully authenticated" not in result.stderr:
    raise RuntimeError(
      "GitHub SSH authentication failed — ensure your key is "
      "uploaded: gh ssh-key list\n"
      f"  (stderr: {result.stderr.strip()!r})"
    )


def check_git_identity():
  name = subprocess.run(
    ["git", "config", "--global", "user.name"],
    capture_output=True, text=True,
  ).stdout.strip()
  email = subprocess.run(
    ["git", "config", "--global", "user.email"],
    capture_output=True, text=True,
  ).stdout.strip()
  if not name or not email:
    raise RuntimeError(
      "git global identity not configured — run:\n"
      '  git config --global user.name "Your Name"\n'
      '  git config --global user.email "you@example.com"'
    )


def main():
  env = _labenv()
  print("=== Preflight Check ===\n")
  check("Python >= 3.10", check_python)
  check("git", lambda: cmd_exists("git"))
  check("gh (GitHub CLI)", lambda: cmd_exists("gh"))
  check("claude (Claude Code CLI)", lambda: cmd_exists("claude"))
  check("requests package", lambda: pkg_exists("requests"))
  check("pyyaml package", lambda: pkg_exists("yaml"))
  for var in NON_SECRET_VARS:
    check(f"{var} in labenv.yaml", lambda v=var: check_labenv_var(env, v))
  check("DISCORD_WEBHOOK_URL set", check_discord_webhook)
  check(f"SSH key {SSH_KEY.name}", check_ssh_key)
  check("SSH to ai-lab", check_ssh)
  check("gh installed", check_gh_install)
  check("gh authenticated", check_gh_auth)
  check(f"GitHub SSH key {GITHUB_SSH_KEY.name}", check_github_ssh_key)
  check("GitHub SSH authentication", check_github_ssh)
  check("git global identity", check_git_identity)
  print("\nAll items must show PASS before the lab begins.")


if __name__ == "__main__":
  main()
