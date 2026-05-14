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
- Set your global git identity — see
  [Git Identity Setup](
  ../tools/dev_workbench/github.md#git-identity-setup)
- Test the SSH connection and verify the greeting — see
  [SSH Validation](
  ../tools/dev_workbench/github.md#ssh-key-setup-for-github)
- Clone `ai_workbench` and create your personal branch — see
  [Clone & Branch](../tools/dev_workbench/github.md#git-command-line-local)

---

## Section 3 — LLM Provider Setup

- [Claude Account Setup](../tools/claude/cloud.md)
- [LLM Provider Cost Control](
  ../tools/dev_workbench/provider_cost_control.md)

Set spending limits and enable usage notifications before running
any multi-turn or automated workflows.

### Multi LLM Provider and Multi Model

Set up alternative LLM providers for the
[Pluggable Models](../sessions/pluggable_models.md) session:

- **Groq** (ultra-fast LPU inference) — see
  [tools/groq/setup.md](../tools/groq/setup.md)
- **OpenRouter** (gateway to 100+ models) — see
  [tools/openrouter/openrouter.md](
  ../tools/openrouter/openrouter.md)
- **Cline** (VSCode AI assistant via OpenRouter) — see
  [tools/dev_workbench/cline.md](
  ../tools/dev_workbench/cline.md)

Install shared Python dependencies — see
[Install OpenAI Python Library](
../tools/dev_workbench/multimodel.md#install-openai-python-library).

---

## Section 4 — VSCode Setup

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

### Claude Multimode

Configure Claude Code for two authentication modes — Pro
Subscription (default) and PAYG API. See
[Claude Multimode Set Up](
../tools/dev_workbench/vscode.md#claude-multimode-set-up).

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
hello, <YourGitHubUser>!
where <YourGitHubUser> is your GitHub username e.g. "joesmith"
```

Claude should create or update the file. Run it to confirm:

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
1. Base: `main` → Compare: `feature/from_<your_username>`
2. Title: `feat: hello.py from <your_username>`
3. Click **Create**.

Expected: PR appears on
`github.com/aiedu-lab/ai_workbench/pulls`.

If all four steps succeed, your development environment is
fully operational.

---

## AI Local

Ollama model files consume disk space but **do not use RAM
when idle** — safe to install now without slowing other
exercises. See [AI Local](ai_local.md) for the full session.

### Set Up

Ollama lets you run open-weight LLMs (Llama, Gemma) entirely
on your laptop — no cloud, no API key, no cost after download.
Follow the guide for your OS:
[Local AI Setup Guide](../tools/ollama/setup.md).

### Test

After installation, verify the model responds:

```bash
ollama run gemma:2b "Hello, who are you?"
```

Expected: a short reply from the local model. Type `/bye`
to exit and free RAM.

## Embedding

Python environment for the Embeddings Visualization session.
See [Exercise: Embeddings Visualization](embedding.md) for
the full session.

### Set Up

Install the Python virtual environment and GloVe dependencies
once before session day — see
[Python venv Setup](../tools/dev_workbench/venv.md) for the
exact commands.

### Test

Verify the environment is ready — see the
[Validation](../tools/dev_workbench/venv.md#validation)
section in the venv setup guide.
