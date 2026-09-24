#!/usr/bin/env bash
# install.sh — one-command, idempotent lab environment setup.
# AI-GENERATED: Phase 50 Step 50.4 (plan.md)
#
# Run after every fresh clone or `git pull` that changes setup:
#   export DISCORD_WEBHOOK_URL="<from #meetup-notifications>"
#   bash miscellaneous/setup/install.sh
#
# Why a shell bootstrap in front of labsetup.py: labsetup.py imports
# requests and yaml at load time, and Ubuntu 26.04's system Python
# refuses pip installs (PEP 668). So this script first builds a
# repo-root .venv holding the pinned setup dependencies, then hands
# off to labsetup.py inside it. All real setup logic stays in
# labsetup.py; this file only guarantees it can start.
#
# Every step is skipped when already satisfied, so reruns are safe.

set -euo pipefail

# Resolve paths from this file, not the caller's cwd, so the script
# works from any directory.
SETUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SETUP_DIR}/../.." && pwd)"
VENV="${REPO_ROOT}/.venv"
REQUIREMENTS="${SETUP_DIR}/requirements.txt"
LABSETUP="${SETUP_DIR}/student/labsetup.py"

say() {
  # Match labsetup.py's "  TAG  message" output style.
  printf '  %-4s %s\n' "$1" "$2"
}

# labsetup.py uses 3.12+ syntax (list[str], X | Y); fail early with a
# clear message instead of a SyntaxError deep inside it.
if ! command -v python3 >/dev/null 2>&1; then
  say "FAIL" "python3 not found — install Python 3.12+ first"
  exit 1
fi
if ! python3 -c 'import sys; sys.exit(sys.version_info < (3, 12))'; then
  say "FAIL" "Python 3.12+ required; found $(python3 -V 2>&1)"
  exit 1
fi
say "OK" "$(python3 -V 2>&1)"

# Ubuntu ships the venv module separately (python3-venv); `import
# ensurepip` is what fails when it is missing.
if ! python3 -c 'import venv, ensurepip' >/dev/null 2>&1; then
  say "APT" "installing python3-venv (sudo)"
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3-venv
fi

# Some project deps (gensim) publish no wheel for the newest Python
# and compile from source, which needs Python.h and a C toolchain.
if ! python3 -c 'import os, sys, sysconfig
sys.exit(not os.path.exists(
  os.path.join(sysconfig.get_paths()["include"], "Python.h")))'; then
  say "APT" "installing python3-dev build-essential (sudo)"
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3-dev build-essential
fi

if [[ -x "${VENV}/bin/python" ]]; then
  say "OK" ".venv already exists (skipping)"
else
  say "VENV" "creating ${VENV}"
  python3 -m venv "${VENV}"
fi

# pip-sync installs exactly the lock (adding, upgrading, and removing
# packages); pip-tools must exist first to provide pip-sync itself.
if [[ ! -x "${VENV}/bin/pip-sync" ]]; then
  say "PIP" "installing pip-tools into .venv"
  "${VENV}/bin/pip" install -q pip-tools
fi
say "PIP" "syncing .venv to $(basename "${REQUIREMENTS}")"
"${VENV}/bin/pip-sync" -q "${REQUIREMENTS}"

say "RUN" "labsetup.py"
"${VENV}/bin/python" "${LABSETUP}" "$@"

say "NEXT" "bash miscellaneous/setup/validate.sh"
