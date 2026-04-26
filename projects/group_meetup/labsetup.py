#!/usr/bin/env python3
"""Parse labenv.yaml and set up the student lab environment.

Steps performed:
1. Load non-confidential env vars from labenv.yaml.
2. Generate ~/.ssh/<username>_id_ed25519 key pair if it does not
   exist (idempotent — skipped if the key is already present).
3. Post the public key to #meetup-notifications so the instructor
   can install it on the Docker server (instructor.md Section 3).
4. Write a ~/.ssh/config entry (Host ai-lab) for the lab server
   (idempotent — skipped if the entry already exists).
5. Validate SSH connectivity to ai-lab.
6. Validate that DISCORD_WEBHOOK_URL is set.

Steps 2–5 are skipped when labenv.yaml still contains placeholder
values (strings wrapped in < >). DISCORD_WEBHOOK_URL must be set
before running — retrieve it from the #meetup-notifications pinned
message posted by the instructor (instructor.md Section 2).
"""
import getpass
import os
import subprocess
import sys
import yaml
import requests
from pathlib import Path

LABENV = Path(__file__).parent / "labenv.yaml"
SECRET_KEY = "DISCORD_WEBHOOK_URL"
SSH_DIR = Path.home() / ".ssh"
SSH_HOST_ALIAS = "ai-lab"

SSH_KEYS = (
  "DOCKER_SERVER_ID",
  "DOCKER_SERVER_USERNAME",
  "DOCKER_SERVER_SSH_PORT",
)

# Use local OS username to name the key so instructors can
# disambiguate public keys from different student laptops.
_USERNAME = getpass.getuser()
SSH_KEY = SSH_DIR / f"{_USERNAME}_id_ed25519"
SSH_CONFIG = SSH_DIR / "config"


def _load_env() -> dict[str, str]:
  with LABENV.open() as f:
    return {k: str(v) for k, v in yaml.safe_load(f).items()}


def _set_env(env: dict[str, str]) -> None:
  for key, value in env.items():
    os.environ[key] = value
    print(f"  SET  {key}={value}")


def _is_placeholder(value: str) -> bool:
  stripped = value.strip()
  return stripped.startswith("<") and stripped.endswith(">")


def _generate_ssh_key() -> None:
  """Generate ed25519 key pair if it does not already exist."""
  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  if SSH_KEY.exists():
    print(f"  OK   SSH key already exists: {SSH_KEY} (skipping)")
    return
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
  server = env.get("DOCKER_SERVER_ID", "<server>")
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
  """Append the ai-lab Host block to ~/.ssh/config.

  Idempotent: does nothing if the Host ai-lab entry already exists.
  """
  existing = SSH_CONFIG.read_text() if SSH_CONFIG.exists() else ""

  # Skip if entry already present
  for line in existing.splitlines():
    if line.strip() == f"Host {SSH_HOST_ALIAS}":
      print(
        f"  OK   ~/.ssh/config entry exists: "
        f"Host {SSH_HOST_ALIAS} (skipping)"
      )
      return

  SSH_DIR.mkdir(mode=0o700, exist_ok=True)
  entry = (
    f"\nHost {SSH_HOST_ALIAS}\n"
    f"  HostName {env['DOCKER_SERVER_ID']}\n"
    f"  User     {env['DOCKER_SERVER_USERNAME']}\n"
    f"  Port     {env['DOCKER_SERVER_SSH_PORT']}\n"
    f"  IdentityFile {SSH_KEY}\n"
  )
  with SSH_CONFIG.open("a") as f:
    f.write(entry)
  SSH_CONFIG.chmod(0o600)
  print(f"  WROTE ~/.ssh/config entry: Host {SSH_HOST_ALIAS}")


def _validate_ssh() -> None:
  result = subprocess.run(
    [
      "ssh", "-o", "BatchMode=yes",
      "-o", "ConnectTimeout=10",
      SSH_HOST_ALIAS, "echo", "ok",
    ],
    capture_output=True,
    text=True,
  )
  if result.returncode != 0 or result.stdout.strip() != "ok":
    print(
      f"\n  WARN SSH to {SSH_HOST_ALIAS!r} not yet available.\n"
      "  Your public key was posted to #meetup-notifications.\n"
      "  Once the instructor confirms it is installed, re-run "
      "this script to validate the connection.\n"
      f"  (stderr: {result.stderr.strip()!r})"
    )
    return
  print(f"  OK   SSH {SSH_HOST_ALIAS} → connection verified")


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


def main() -> None:
  env = _load_env()
  _set_env(env)

  ssh_real = all(
    k in env and not _is_placeholder(env[k]) for k in SSH_KEYS
  )

  if ssh_real:
    _generate_ssh_key()
    _post_pubkey_to_discord(env)
    _write_ssh_config(env)
    _validate_ssh()
  else:
    print(
      "  SKIP SSH setup — labenv.yaml still has placeholder values.\n"
      "  Fill in DOCKER_SERVER_ID, DOCKER_SERVER_USERNAME, and\n"
      "  DOCKER_SERVER_SSH_PORT with real values, then re-run."
    )

  _validate_secret()
  print("\nEnvironment ready.")


if __name__ == "__main__":
  main()
