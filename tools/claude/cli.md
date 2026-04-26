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

The CLI supports two modes. Use **API Key** for this lab.

#### API Key Mode (recommended for lab)
```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # set once per session
unset CLAUDE_CODE_OAUTH_TOKEN           # ensure OAuth is not active
```

#### Subscription / OAuth Token Mode
```bash
# OAuth token takes precedence over API key when both are set.
# Obtain via: claude setup-token  (valid for one year)
export CLAUDE_CODE_OAUTH_TOKEN="sk-any-..."
```

#### Validate Auth Status
```bash
claude auth status --text
```

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

Once installed:

* Click the **Spark (⚡) icon** in the left Activity Bar to open the Claude Code sidebar
* The same icon appears in the top-right Editor Toolbar when a file is open
* Inline diffs appear in real time — use **Accept / Reject** buttons per change
* Open multiple conversations in separate tabs via the Sessions list

To keep the sidebar open across restarts, add to your VSCode `settings.json`:

```json
{
  "auto-run-command.rules": [
    {
      "condition": "always",
      "command": "claude-vscode.sidebar.open"
    }
  ]
}
```

Or set a keyboard shortcut: `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Windows).

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
claude plugin update
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

## 🔐 Security: API Keys

> See [Claude Cloud Setup — API Key](cloud.md#2-generate-an-api-key)
> for key creation, storage, and revocation instructions.

- NEVER commit API keys to GitHub
- Use `ANTHROPIC_API_KEY` environment variable only

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../provider_cost_control.md#pay-per-use)

## Documentation

[Claude Code (CLI)](https://code.claude.com/docs)
