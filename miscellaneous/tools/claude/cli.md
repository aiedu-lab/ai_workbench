# Claude Code CLI

## CLI Setup

Run in terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Restart terminal after install.

## 🧭 Authenticate

> **Account and API key setup:** See [Claude Cloud Setup](cloud.md)
> for account creation, API key generation, `ANTHROPIC_API_KEY` env
> var, and privacy settings. Complete that guide first.

### 1. Choose CLI auth mode

The CLI supports two modes. Use **OAuth Token Mode** for this lab.

#### Subscription / OAuth Token Mode 
Recommended as primary access mode for lab:
```bash
# OAuth token takes precedence over API key when both are set
claude setup-token # generate a one year valid OAUTH TOKEN
# set as env variable and persist across terminal sessions:
echo 'export MY_CLAUDE_CODE_OAUTH_TOKEN="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

#### API Key Mode 
Recommended as backup or "overflow" access mode for lab
```bash
# set as env variable and persist across terminal sessions:
echo 'export MY_ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```
#### Convenience functions to switch modes

Claude Code supports three authentication modes, selected by
environment variables.

Add to `~/.bashrc`:

```bash
#
# Credentials and entitlements depends on from where it was picked -
# 1) ~/.credentials/.credentials.json - personal user agent case
# 2) MY_CLAUDE_CODE_OAUTH_TOKEN - headless use - subscription mode inferencing
# 3) MY_ANTHROPIC_API_KEY - pay-as-you-go API key
#
#
# By default Do NOT enable either API KEY (PAYG) or OAUTH TOKEN
#
# $HOME/.claude/.credentials.json is for interactive human
# use on a persistent machine;
#
# Whereas CLAUDE_CODE_OAUTH_TOKEN is for automated/headless use
# where you accept the inference-only tradeoff in exchange
# for portability.
#
# Enable OAUTH TOKEN only when using headless mode
# Enable API KEY only when you have exhausted subscription mode
# and want to continue until tokens are refreshed
#
# Convenience functions to switch claude modes:
#
# Long lived oAuth Token - Subscription
claude-subscribe() {
  unset ANTHROPIC_API_KEY
  export CLAUDE_CODE_OAUTH_TOKEN="$MY_CLAUDE_CODE_OAUTH_TOKEN"
  claude auth logout && claude auth login
  echo "claude set to - `claude auth status --text` - mode"
  # shows: 'Auth token: CLAUDE_CODE_OAUTH_TOKEN'
}
# API Key - PAYG
claude-api() {
  unset CLAUDE_CODE_OAUTH_TOKEN
  export ANTHROPIC_API_KEY="$MY_ANTHROPIC_API_KEY"
  claude auth logout && claude auth login
  echo "claude set to - `claude auth status --text` - mode"
  # first line shows: 'API key: /login managed key'
}
# Auth picked up from Local Credentials that is set by last
# `claude auth login` mode
# Default Mode is Local
claude-local() {
  unset CLAUDE_CODE_OAUTH_TOKEN && unset ANTHROPIC_API_KEY
  claude auth logout && claude auth login
  echo "claude set to - `claude auth status --text` - mode"
  # first line shows: 'Login method: Claude Pro/Max account'
}
```

#### Validation

```bash
echo "Initial claude code mode"
claude auth status --text

echo "Switching claude code to API PAYG mode"
# must print api key (not empty)
claude-api && \
  echo "ANTHROPIC_API_KEY is \"$ANTHROPIC_API_KEY\"" && \
  claude auth status --text

echo "Switching claude code to OAUTH Subscription mode"
# must print auth token (not empty)
claude-subscribe && \
  echo "CLAUDE_CODE_OAUTH_TOKEN is \"$CLAUDE_CODE_OAUTH_TOKEN\"" && \
  claude auth status --text

echo "Initial claude code mode"
claude auth status --text
```

> **NEVER** add these key to any file that is committed to Git.
> Add `.env` to `.gitignore` if you store keys in a local `.env`
> file.

### 2. Login via browser (first time only)

```bash
claude logout   # clear any stale session
claude          # opens browser auth flow on first run
```

### 3. Always run inside the repo

```bash
cd ai_workbench
```

### 4. Verify environment

```bash
bash tools/claude/check_env.sh
claude
```

### 5. Install the VSCode Extension

* Open VSCode
* Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac) to open    Extensions
* Search for **"Claude Code"** — install the extension published by **Anthropic** (2M+ installs, verified publisher)
* Restart VSCode if prompted

### 6. Confirm the integrated terminal works

In VSCode's integrated terminal (`Ctrl+\``):

```bash
claude -p "say hello" 
```

You should see an example response as below. The CLI and the extension share the same
authentication and settings.

```bash
Hello! How can I help you today?
```

### 7. Constrain scope in prompts

Always include:

"Only read files in this project directory. Do not access external folders."

### 8. Avoid large directories

Never run on:
* ~/
* Downloads/
* node_modules/

### 9. Kill runaway processes

Press:

* Ctrl + C (Windows/Linux)
* Cmd + . (Mac)

---

## Plugin Installs 

```bash
# Step 1 — Add the demo marketplace (one-time):
claude plugin marketplace add anthropics/claude-code
# Note: adds as "claude-code-plugins" (not "anthropics-claude-code")

# Step 2 — Install code-review from demo marketplace:
claude plugin install code-review@claude-code-plugins

# Step 3 — Install pr-review-toolkit from official marketplace:
claude plugin install pr-review-toolkit@claude-plugins-official

# Step 4 - Verify all plugins installed
# Should show the below two: 
# - code-review@claude-code-plugins
# - pr-review-toolkit@claude-plugins-official
claude plugin list

# Step 5 - Verify the marketplaces available
# Should show the below two:
# claude-code-plugins  
# claude-plugins-official
ls ~/.claude/plugins/marketplaces/

# Step 6 - Update all plugins
# Native plugins are auto-updated, 3rd party require manual updates
claude plugin marketplace update claude-code-plugins
claude plugin marketplace update claude-plugins-official
```

---

## When to Use CLI vs VSCode Extension vs Desktop

| Project Type | Recommended Route | Why |
|---|---|---|
| **Simple** — single file, quick fix, scripted output | **CLI** | Fastest; pipe output directly; scriptable |
| **Medium** — multi-file feature, incremental changes | **VSCode Extension** | Inline diffs, accept/reject per change, file navigation sidebar |
| **Complex** — large refactor, migration, multi-agent | **VSCode Extension + CLI** | Extension for review; CLI for automation, hooks, and scripting |
| **Non-technical user, rapid prototype** | **Claude Desktop (Chat)** | No terminal required; conversational interface |
| **CI/CD pipeline / automation** | **CLI with `-p` flag** | Non-interactive, scriptable, redirect-friendly |

**Rule of thumb:**

* Writing a new file from a prompt → **CLI**
* Reviewing and editing existing code → **VSCode Extension**
* Planning a large change before executing → **Desktop (Chat)** or
  Extension Plan Mode (`Shift+Tab` twice)

---

## 🔐 Security: OAuth Token and API Keys

> Reference section above `Subscription / OAuth Token Mode`
> for oauth token creation, storage, etc.
> OR
> See [Claude Cloud Setup — API Key](cloud.md#2-generate-an-api-key)
> for key creation, storage, and revocation instructions.

- NEVER commit OAUTH TOKEN or API keys to GitHub
- Use environment variables only — never hardcode keys or tokens

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../dev_workbench/provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../dev_workbench/provider_cost_control.md#pay-per-use)

## Documentation

[Claude Code (CLI)](https://code.claude.com/docs)
