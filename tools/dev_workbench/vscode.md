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
## Claude Multimode Set Up

Claude Code supports two authentication modes, selected by
environment variables. `CLAUDE_CODE_OAUTH_TOKEN` (Pro/Max
subscription) takes precedence over `ANTHROPIC_API_KEY`
(pay-as-you-go) when both are set; unset the token to fall
back to the API key.

### Convenience functions

Add to `~/.bashrc`:

```bash
# MY_CLAUDE_CODE_OAUTH_TOKEN is the Pro/Max subscription token
# MY_ANTHROPIC_API_KEY is the pay-as-you-go API key

claude-subscribe() {
  unset ANTHROPIC_API_KEY
  export CLAUDE_CODE_OAUTH_TOKEN="$MY_CLAUDE_CODE_OAUTH_TOKEN"
  echo "claude set to - $(claude auth status --text) - mode"
}
claude-api() {
  unset CLAUDE_CODE_OAUTH_TOKEN
  export ANTHROPIC_API_KEY="$MY_ANTHROPIC_API_KEY"
  echo "claude set to - $(claude auth status --text) - mode"
}

# Default to subscription mode — OAuth token takes precedence
# when both are set
export CLAUDE_CODE_OAUTH_TOKEN="$MY_CLAUDE_CODE_OAUTH_TOKEN"
```

Launch VSCode from the Ubuntu terminal:

```bash
code .
```

### Validation

Inside the Claude Code panel, run `/status` — the output shows
the active authentication mode (Pro Subscription or API key).

## Guardrails
* If using WAL, always work inside WSL directory `~/` rather than 
  Windows paths `/mnt/c/...` as cross-filesystem I/O is significantly 
  slower and may cause permission issues.
