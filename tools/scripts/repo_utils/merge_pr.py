# ===================================================================
# tools/scripts/repo_utils/merge_pr.py
# ===================================================================
"""Merges a pull request via `gh pr merge`, after explicitly
confirming it's actually safe to merge rather than trusting gh's own
opaque mergeable/mergeStateStatus fields. Deliberately human-invoked
only: this merges a real PR into a real branch, so it must only ever
run when a human explicitly invokes it with an explicit PR number --
never wired to a hook, CI, or any other automatic trigger.

This repo has no bazel setup, so this runs via plain `python3` --
see _pr_utils.py's docstring for why find_repo_root() walks up from
its own file depth instead of `BUILD_WORKSPACE_DIRECTORY`.

Checks performed before merging:
  a) every check run has finished, and none of them failed
  b) either no review is required (reviewDecision is empty -- the
     common case on a repo that can't turn on required reviews at
     all, e.g. a private repo on GitHub's Free plan) or one is
     required and has already been satisfied (reviewDecision ==
     APPROVED)

Run via:
  python3 tools/scripts/repo_utils/merge_pr.py 123
  python3 tools/scripts/repo_utils/merge_pr.py 123 --method squash \
      --delete-branch
"""

import argparse
import subprocess
import sys

from _pr_utils import (
  check_auth_and_permission,
  fetch_pr_status,
  find_repo_root,
)

MIN_PERMISSION = {"WRITE", "MAINTAIN", "ADMIN"}


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("pr_number", type=int)
  parser.add_argument(
    "--method", choices=["merge", "squash", "rebase"], default="merge"
  )
  parser.add_argument("--delete-branch", action="store_true")
  return parser.parse_args()


def check_mergeable(workspace_root, pr_number):
  data = fetch_pr_status(workspace_root, pr_number, "merge_pr")

  if data["state"] != "OPEN":
    print(
      f"merge_pr: PR #{pr_number} is {data['state']}, not OPEN -- "
      "nothing to merge.",
      file=sys.stderr,
    )
    sys.exit(1)

  pending = data["pending_checks"]
  if pending:
    print(
      f"merge_pr: {len(pending)} check(s) still running on PR "
      f"#{pr_number}: {', '.join(pending)} -- wait for them to "
      "finish before merging.",
      file=sys.stderr,
    )
    sys.exit(1)

  failed = data["failed_checks"]
  if failed:
    print(
      f"merge_pr: {len(failed)} check(s) failed on PR #{pr_number}: "
      f"{', '.join(failed)} -- fix them before merging.",
      file=sys.stderr,
    )
    sys.exit(1)

  review_decision = data["reviewDecision"]
  if review_decision not in ("", "APPROVED"):
    note = ""
    if review_decision == "REVIEW_REQUIRED":
      note = (
        " (note: if you opened this PR, GitHub won't let you "
        "approve your own -- a different collaborator needs to.)"
      )
    print(
      f"merge_pr: PR #{pr_number} requires a review that hasn't "
      f"been satisfied yet (reviewDecision={review_decision}).{note}",
      file=sys.stderr,
    )
    sys.exit(1)


def main():
  args = parse_args()
  workspace_root = find_repo_root()

  check_auth_and_permission(workspace_root, MIN_PERMISSION, "merge_pr")
  check_mergeable(workspace_root, args.pr_number)

  merge_cmd = ["gh", "pr", "merge", str(args.pr_number), f"--{args.method}"]
  if args.delete_branch:
    merge_cmd.append("--delete-branch")
  result = subprocess.run(merge_cmd, cwd=workspace_root)
  sys.exit(result.returncode)


if __name__ == "__main__":
  main()
