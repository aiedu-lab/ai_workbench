# Development Workbench

<!-- AI-GENERATED: Phase 14 Step 14.1.1
     (miscellaneous/software_defined_workbench/plan.md) -->

This session walks every student through a one-time platform and
tooling setup. Both supported platforms produce an identical Ubuntu
environment — the only difference is the virtualisation layer.

---

## Concept

> **VS Code is your interface. Your code runs in Linux.**

Both platforms give you the same Ubuntu shell, the same Claude
plugin experience, and the same SSH access to the shared lab server.

---

## Platform Overview

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

## VM / Container Setup

[VM Setup Guide](../miscellaneous/tools/VM/setup.md)

- **Win11:** install WSL2 + Ubuntu 22.04; verify with `wsl --status`
- **macOS:** install Docker Desktop + Dev Containers extension;
  open repo in VSCode → "Reopen in Container"

---

## GitHub Account and SSH Setup

[GitHub Setup Guide](../miscellaneous/tools/dev_workbench/github_and_git.md)

- Create a GitHub account at `github.com`
- Install the `gh` CLI inside Ubuntu (WSL2 or Dev Container) —
  full steps in the
  [GitHub Setup Guide](
  ../miscellaneous/tools/dev_workbench/github_and_git.md#account-setup)
- [Generate and upload an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
  for GitHub authentication
- Set your global git identity — see
  [Git Identity Setup](
  ../miscellaneous/tools/dev_workbench/github_and_git.md#git-identity-setup)
- Test the SSH connection and verify the greeting — see
  [SSH Validation](
  ../miscellaneous/tools/dev_workbench/github_and_git.md
  #ssh-key-setup-for-github)
- Clone `ai_workbench` and create your personal branch — see
  [Clone & Branch](../miscellaneous/tools/dev_workbench/github_and_git.md#git-command-line-local)

---

## LLM Provider Setup

| Tool | Setup guide |
|------|-------------|
| Claude Account Setup | [cloud account](../miscellaneous/tools/claude/cloud.md) |
| Claude Code CLI | [cli](../miscellaneous/tools/claude/cli.md) | 
| Claude Desktop (Chat + CoWork) | [desktop](../miscellaneous/tools/claude/desktop.md) |

### Advanced & Optional
* Reference [LLM Provider Cost Control](../miscellaneous/tools/dev_workbench/provider_cost_control.md)
* Set spending limits and enable usage notifications before running
any multi-turn or automated workflows.

### Multi LLM Provider and Multi Model

Set up alternative LLM providers for the
[Pluggable Models](../sessions/pluggable_models.md) session:

- **Groq** (ultra-fast LPU inference) — see
  [miscellaneous/tools/groq/setup.md](../miscellaneous/tools/groq/setup.md)
- **OpenRouter** (gateway to 100+ models) — see
  [miscellaneous/tools/openrouter/openrouter.md](
  ../miscellaneous/tools/openrouter/openrouter.md)
- **Cline** (VSCode AI assistant via OpenRouter) — see
  [miscellaneous/tools/dev_workbench/cline.md](
  ../miscellaneous/tools/dev_workbench/cline.md)

Install shared Python dependencies — see
[Install OpenAI Python Library](
../miscellaneous/tools/dev_workbench/multimodel.md
#install-openai-python-library).

---

## VSCode Setup

[VSCode Setup Guide](../miscellaneous/tools/dev_workbench/vscode.md)

- Install VSCode on your host OS
- **Win11:** install **Remote - WSL** extension
- **macOS:** install **Dev Containers** extension
- Open VSCode project from **Ubuntu terminal**: `code .`
- Install and sign in to the **Claude Code** extension
- Install and sign in to the **GitHub Pull Requests** extension —
  full steps in
  [VSCode Setup Guide](../miscellaneous/tools/dev_workbench/vscode.md#setup)
- Validate both extensions per
  [VSCode Validation](
  ../miscellaneous/tools/dev_workbench/vscode.md#validation)

### Claude Multimode

Configure Claude Code for two authentication modes — Pro
Subscription (default) and PAYG (pay-as-you-go) API. See
[Claude Multimode Set Up](
../miscellaneous/tools/dev_workbench/vscode.md#claude-multimode-set-up).

---

## Test VSCode + GitHub + Claude Code Integration

Validate the full round-trip: Pull → Claude edits → Push → PR.

**Step 0 — Switch to your personal feature branch:**

In the VSCode terminal:

```bash
# switch to a feature branch, create if not created before
export GITHUB_USERNAME=`gh api user -q .login`
git switch feature/from_$GITHUB_USERNAME || \
  git switch -c feature/from_$GITHUB_USERNAME
```

**Step 1 — Pull latest code from your personal branch:**

In VSCode, open the Source Control panel (`Ctrl+Shift+G`).
Click the **⋯** menu → **Pull**. Confirm no errors.

**Step 2 — Use Claude Code to update `miscellaneous/tests/vscode/hello.py`:**

Open the Claude Code panel in VSCode and send this prompt:

```text
Update miscellaneous/tests/vscode/hello.py to print:
hello, joesmith!
where joesmith is your GitHub username
```

Claude should create or update the file. Run it to confirm:

```bash
python3 miscellaneous/tests/vscode/hello.py
```

Expected output: `hello, <your_github_username>!`

**Step 3 — Push the change to your personal branch:**

In the Source Control panel:
1. Stage `miscellaneous/tests/vscode/hello.py` (click the `+` icon).
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

## Run Lab Setup Script

Retrieve the Discord webhook URL from `#meetup-notifications`,
then run both scripts from inside Ubuntu:

```bash
export DISCORD_WEBHOOK_URL="<paste from #meetup-notifications>"
python3 miscellaneous/setup/student/labsetup.py
python3 miscellaneous/setup/student/preflight_check.py
```

`labsetup.py` generates your SSH key pair, posts your public key
to Discord, writes the `ai-lab` SSH config entry, and installs
CLI tools required by optional sessions (poppler-utils,
html2text).
Every item in `preflight_check.py` output must show **PASS**.

---
## Additional Setups

**ALL** the below setups are automatically effected when you
ran the [lab setup script](miscellaneous/setup/student/labsetup.py)
above.

### AI Local

Ollama model files consume disk space but **do not use RAM
when idle** — safe to install now without slowing other
exercises. See [AI Local](ai_local.md) for the full session.

#### Set Up

Reference [Run Lab Setup Script](#run-lab-setup-script) - 
it installs Ollama automatically.

To install manually, follow the guide for your OS:
[Local AI Setup Guide](../miscellaneous/tools/ollama/setup.md).

#### Test

After installation, verify the model responds:

```bash
ollama run gemma:2b "Hello, who are you?"
```

Expected: a short reply from the local model. Type `/bye`
to exit and free RAM.

---

### Embedding

Python environment for the Embeddings Visualization session.
See [Exercise: Embeddings Visualization](embedding.md) for
the full session.

#### Set Up

Reference [Run Lab Setup Script](#run-lab-setup-script) - 
it creates the Python virtual environment, installs
all dependencies, and registers the Jupyter kernel automatically.

To set up manually, see
[Python venv Setup](../miscellaneous/tools/dev_workbench/venv.md).

#### Test

Verify the environment is ready — see the
[Validation](../miscellaneous/tools/dev_workbench/venv.md#validation)
section in the venv setup guide.

### PKM

Speed Reading Mindmap converts a PDF or text book into an
interactive HTML mind-map using a multi-agent pipeline.
See [LLM Wiki — Speed Reading Extension](llm_wiki.md) for
the full session.

#### Set Up

Reference [Run Lab Setup Script](#run-lab-setup-script) - 
it handles installation and all PKM dependencies 
automatically:

- Installs `poppler-utils` (`pdftotext`) and `html2text`
  CLI tools via `apt`.
- Creates `projects/llm_wiki/speed-reading/.venv` for
  `src/piper.py` (Python stdlib only — no pip packages).

To install CLI tools manually:

```bash
sudo apt install poppler-utils html2text
```

To create the piper venv manually:

```bash
python3 -m venv projects/llm_wiki/speed-reading/.venv
```

#### Test

After setup, verify CLIs and piper.py are ready:

```bash
which pdftotext && which html2text
python3 projects/llm_wiki/speed-reading/src/piper.py --help
```

Expected: both CLIs print their paths; `piper.py --help`
prints the PHASES section.
