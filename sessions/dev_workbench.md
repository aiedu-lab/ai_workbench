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

## Section 2 — VSCode Setup

[VSCode Setup Guide](../tools/dev_workbench/vscode.md)

- Install VSCode on your host OS
- **Win11:** install **Remote - WSL** extension
- **macOS:** install **Dev Containers** extension
- Install the **Claude** extension inside VSCode
- Open project from Ubuntu terminal: `code .`

---

## Section 3 — GitHub Account and SSH Setup

[GitHub Setup Guide](../tools/dev_workbench/github.md)

- Create a GitHub account at `github.com`
- Generate and upload an SSH key for GitHub authentication
- Set your global git identity inside Ubuntu:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

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

## Section 6 — Test Claude Validation

1. Open the Claude plugin panel in VSCode.
2. Prompt: `"Write a hello_world.py that prints Hello, World!"`
3. Accept the generated file, then run it from the terminal:

```bash
python3 hello_world.py
```

Expected output: `Hello, World!`

If Claude generates the file and it runs correctly, your
development environment is fully operational.
