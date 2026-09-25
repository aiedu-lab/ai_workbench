#!/usr/bin/env bash
# validate.sh — read-only check that the lab environment is ready.
# AI-GENERATED: Phase 50 Step 50.5 (plan.md)
#
# Run after install.sh (and any time something seems off):
#   bash miscellaneous/setup/validate.sh
#
# Exit status: 0 = every check PASS, 1 = at least one FAIL (from
# preflight_check.py), 2 = .venv missing, so install.sh never ran.
# It runs preflight_check.py inside the repo-root .venv because that
# script imports yaml, which install.sh provides there; all check
# logic stays in preflight_check.py. Installs and changes nothing.

set -euo pipefail

SETUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SETUP_DIR}/../.." && pwd)"
VENV_PY="${REPO_ROOT}/.venv/bin/python"

if [[ ! -x "${VENV_PY}" ]]; then
  echo "  FAIL .venv not found — run miscellaneous/setup/install.sh first"
  exit 2
fi

# exec so preflight_check.py's exit status is this script's status.
exec "${VENV_PY}" "${SETUP_DIR}/student/preflight_check.py" "$@"
