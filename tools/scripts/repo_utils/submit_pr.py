# ===================================================================
# tools/scripts/repo_utils/submit_pr.py
# ===================================================================
"""Pushes the current branch and opens a pull request via `gh pr
create`. Deliberately human-invoked only: this pushes to a real
remote and opens a real PR, so it must only ever run when a human
explicitly invokes it with explicit arguments -- never wired to a
hook, CI, or any other automatic trigger.

This repo has no bazel setup, so this runs via plain `python3`, not
`bazel run` -- see _pr_utils.py's docstring for why find_repo_root()
walks up from its own known file depth instead of the
`BUILD_WORKSPACE_DIRECTORY` mechanism ../ITDev's version of this
file uses.

Run via:
  python3 tools/scripts/repo_utils/submit_pr.py \
      --title "<title>" --body "<body>"
  python3 tools/scripts/repo_utils/submit_pr.py \
      --title "..." --body "..." --base main --draft
"""

import argparse
import subprocess
import sys

from _pr_utils import check_auth_and_permission, find_repo_root, run

# GitHub's viewerPermission values, highest to lowest: ADMIN,
# MAINTAIN, WRITE, TRIAGE, READ, NONE. Submitting a PR needs push
# access to open a branch-backed PR.
MIN_PERMISSION = {"WRITE", "MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--title", required=True)
  parser.add_argument("--body", required=True)
  parser.add_argument("--base", default="main")
  parser.add_argument("--draft", action="store_true")
  return parser.parse_args()


def main():
  args = parse_args()
  workspace_root = find_repo_root()

  check_auth_and_permission(workspace_root, MIN_PERMISSION, "submit_pr")

  branch = run(
    ["git", "branch", "--show-current"], workspace_root
  ).stdout.strip()
  if not branch:
    print(
      "submit_pr: not on a branch (detached HEAD) -- aborting.",
      file=sys.stderr,
    )
    sys.exit(1)
  if branch == args.base:
    print(
      f"submit_pr: current branch is '{branch}', same as --base "
      "-- aborting.",
      file=sys.stderr,
    )
    sys.exit(1)

  status = run(["git", "status", "--porcelain"], workspace_root).stdout
  if status.strip():
    print(
      "submit_pr: working tree is not clean -- commit or stash "
      "changes first.",
      file=sys.stderr,
    )
    sys.exit(1)

  print(f"submit_pr: pushing '{branch}' to origin...")
  push_result = subprocess.run(
    ["git", "push", "-u", "origin", branch], cwd=workspace_root
  )
  if push_result.returncode != 0:
    sys.exit(push_result.returncode)

  create_cmd = [
    "gh",
    "pr",
    "create",
    "--title",
    args.title,
    "--body",
    args.body,
    "--base",
    args.base,
  ]
  if args.draft:
    create_cmd.append("--draft")
  create_result = subprocess.run(create_cmd, cwd=workspace_root)
  sys.exit(create_result.returncode)


if __name__ == "__main__":
  main()
