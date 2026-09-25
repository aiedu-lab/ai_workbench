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
# It first checks the manual prerequisites in prerequisites.md and
# stops, changing nothing, if any are missing. Every later step is
# skipped when already satisfied, so reruns are safe.

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

# Prerequisite gate (AI-GENERATED: Phase 50 Step 50.11): check every
# manual step marked "yes" in prerequisites.md before changing
# anything, so a blank account stops here with the full list instead
# of failing halfway through the install.

# labsetup.py uses 3.12+ syntax (list[str], X | Y).
has_python() {
  command -v python3 &&
    python3 -c 'import sys; sys.exit(sys.version_info < (3, 12))'
}
has_git_identity() {
  command -v git &&
    [[ -n "$(git config --global user.name)" ]] &&
    [[ -n "$(git config --global user.email)" ]]
}
# labsetup.py uploads the GitHub SSH key through an authenticated gh.
has_gh_auth() {
  command -v gh && gh auth status
}
# Presence only: the webhook value is a secret and is never printed.
has_webhook() {
  [[ -n "${DISCORD_WEBHOOK_URL:-}" ]]
}

missing=0
require() {
  # Usage: require LABEL CHECK_FUNCTION — prints OK or MISS.
  if "$2" >/dev/null 2>&1; then
    say "OK" "$1"
  else
    say "MISS" "$1"
    missing=$((missing + 1))
  fi
}
require "Python 3.12+" has_python
require "git with global user.name and user.email" has_git_identity
require "gh installed and authenticated (gh auth login)" has_gh_auth
require "DISCORD_WEBHOOK_URL exported" has_webhook
if ((missing > 0)); then
  say "STOP" "${missing} prerequisite(s) missing; nothing was changed."
  say "SEE" "miscellaneous/setup/prerequisites.md"
  exit 1
fi

# Ubuntu ships the venv module separately (python3-venv); `import
# ensurepip` is what fails when it is missing.
if ! python3 -c 'import venv, ensurepip' >/dev/null 2>&1; then
  say "APT" "installing python3-venv (sudo)"
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3-venv
fi

# A project dep with no wheel for the newest Python compiles from
# source, which needs Python.h and a C toolchain.
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
