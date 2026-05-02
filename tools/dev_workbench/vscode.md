# VSCode

## Setup
* [VSCode](https://code.visualstudio.com/download)
  - During install, check "Add to PATH"
  - After install, open VSCode and install:
* [Remote-WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) (Microsoft) - if using WSL
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (Microsoft)
* [Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) (Anthropic)
* **GitHub Extension** — built-in Source Control; no extra install
  needed. Sign in: Accounts icon (bottom-left) → "Sign in with
  GitHub" → authorize in browser.
* **GitHub Pull Requests Extension**:
  1. Extensions (`Ctrl+Shift+X`) → search "GitHub Pull Requests"
  2. Install **GitHub Pull Requests** (GitHub, Inc.)
  3. Sign in: click the GitHub icon in the Activity Bar →
     "Sign In" → authorize in browser.

## Validation

### VSCode and CLI Basics
* Open your `ai_workbench` folder from Ubuntu terminal: `code .`
* Verify Claude CLI: `claude --version`

### GitHub Extension
* Run from Ubuntu terminal: `git branch --all`
  — your personal branch (`feature/from_<username>`) should appear.
* Use VSCode Source Control panel: `git pull` and `git push`
  work without entering credentials.

### GitHub Pull Request Extension
* Click the GitHub icon in the Activity Bar.
* The **Pull Requests** and **Issues** panels are visible.
* Your personal branch appears under "Current Branch".
## Guardrails
* If using WAL, always work inside WSL directory `~/` rather than 
  Windows paths `/mnt/c/...` as cross-filesystem I/O is significantly 
  slower and may cause permission issues.
