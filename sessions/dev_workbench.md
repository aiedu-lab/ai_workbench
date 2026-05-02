# Development Workbench

<!-- AI-GENERATED: Phase 14 Step 14.1.1 (sdw/plan.md) -->

This session walks every student through a one-time platform and
tooling setup. Both supported platforms produce an identical Ubuntu
environment — the only difference is the virtualisation layer.

---

## Concept

> **VS Code is your interface. Your code runs in Linux.**

Both platforms give you the same Ubuntu shell, the same Claude
plugin experience, and the same SSH access to the shared lab server.

---

## Section 0 — Platform Overview

| Layer | Win11 | macOS |
|-------|-------|-------|
| Frontend | VSCode native | VSCode native |
| Dev environment | WSL2 Ubuntu | Dev Container Ubuntu |
| Server access | SSH → `ai-lab` | SSH → `ai-lab` (identical) |

> Both paths produce an identical Ubuntu shell. Every command in
> this session works on both platforms unless noted otherwise.

---

## Exercise

Complete each section in order. Every section links to the detailed
guide for that tool — no content is duplicated here.

---

## Section 1 — VM / Container Setup

[VM Setup Guide](../tools/VM/setup.md)

- **Win11:** install WSL2 + Ubuntu 22.04; verify with `wsl --status`
- **macOS:** install Docker Desktop + Dev Containers extension;
  open repo in VSCode → "Reopen in Container"

---

## Section 2 — GitHub Account and SSH Setup

[GitHub Setup Guide](../tools/dev_workbench/github.md)

- Create a GitHub account at `github.com`
- Install the `gh` CLI inside Ubuntu (WSL2 or Dev Container) —
  full steps in the
  [GitHub Setup Guide](../tools/dev_workbench/github.md#account-setup)
- Generate and upload an SSH key for GitHub authentication
- Set your global git identity inside Ubuntu:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

- Test the SSH connection directly without using any git commands:

```bash
ssh -T git@github.com
```

- Validate: you'll receive a greeting if the key is provisioned:

```text
Hi [GitHub Username]! You've successfully authenticated...
```

- Clone `ai_workbench` and create your personal branch — see
  [Clone & Branch](../tools/dev_workbench/github.md#git-command-line-local)

---

## Section 3 — VSCode Setup

[VSCode Setup Guide](../tools/dev_workbench/vscode.md)

- Install VSCode on your host OS
- **Win11:** install **Remote - WSL** extension
- **macOS:** install **Dev Containers** extension
- Open VSCode project from **Ubuntu terminal**: `code .`
- Install and sign in to the **Claude Code** extension
- Install and sign in to the **GitHub Pull Requests** extension —
  full steps in
  [VSCode Setup Guide](../tools/dev_workbench/vscode.md#setup)
- Validate both extensions per
  [VSCode Validation](../tools/dev_workbench/vscode.md#validation)

---

## Section 4 — LLM Provider Setup

- [Claude Account Setup](../tools/claude/cloud.md)
- [LLM Provider Cost Control](../tools/dev_workbench/provider_cost_control.md)

Set spending limits and enable usage notifications before running
any multi-turn or automated workflows.

---

## Section 5 — Run Lab Setup Script

Retrieve the Discord webhook URL from `#meetup-notifications`,
then run both scripts from inside Ubuntu:

```bash
export DISCORD_WEBHOOK_URL="<paste from #meetup-notifications>"
python3 projects/group_meetup/labsetup.py
python3 projects/group_meetup/preflight_check.py
```

`labsetup.py` generates your SSH key pair, posts your public key
to Discord, and writes the `ai-lab` SSH config entry.
Every item in `preflight_check.py` output must show **PASS**.

---

## Section 6 — Test VSCode + GitHub + Claude Code Integration

Validate the full round-trip: Pull → Claude edits → Push → PR.

**Step 1 — Pull latest code from your personal branch:**

In VSCode, open the Source Control panel (`Ctrl+Shift+G`).
Click the **⋯** menu → **Pull**. Confirm no errors.

**Step 2 — Use Claude Code to update `tests/vscode/hello.py`:**

Open the Claude Code panel in VSCode and send this prompt:

```text
Update tests/vscode/hello.py to print:
hello, <my_github_username>!
Replace <my_github_username> with my actual GitHub username.
```

Claude will create or update the file. Run it to confirm:

```bash
python3 tests/vscode/hello.py
```

Expected output: `hello, <your_github_username>!`

**Step 3 — Push the change to your personal branch:**

In the Source Control panel:
1. Stage `tests/vscode/hello.py` (click the `+` icon).
2. Enter a commit message: `feat: add hello.py`
3. Click **Commit**, then **Sync Changes** (push).

**Step 4 — Submit a Pull Request to `main`:**

In the Activity Bar, click the **GitHub** icon.
Under **Pull Requests**, click **Create Pull Request**.
- Base: `main` → Compare: `feature/from_<your_username>`
- Title: `feat: hello.py from <your_username>`
- Click **Create**.

Expected: PR appears on
`github.com/aiedu-lab/ai_workbench/pulls`.

If all four steps succeed, your development environment is
fully operational.
