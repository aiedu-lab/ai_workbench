import importlib
import os
import subprocess
import sys


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


def check_webhook():
  if not os.environ.get("DISCORD_WEBHOOK_URL"):
    raise RuntimeError("DISCORD_WEBHOOK_URL not set")


print("=== Preflight Check ===\n")
check("Python >= 3.10", check_python)
check("git", lambda: cmd_exists("git"))
check("gh (GitHub CLI)", lambda: cmd_exists("gh"))
check("claude (Claude Code CLI)", lambda: cmd_exists("claude"))
check("requests package", lambda: pkg_exists("requests"))
check("pyyaml package", lambda: pkg_exists("yaml"))
check("DISCORD_WEBHOOK_URL set", check_webhook)
print("\nAll items must show PASS before the lab begins.")
