# Claude Code CLI

## CLI Setup

Run in terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Restart terminal after install.

## 🧭 Authenticate

1. Provision Claude Platform
* [Login Claude Platform](https://platform.claude.com/)
* [Purchase $5 Credits](https://platform.claude.com/billing)
* [Generate and copy API key](https://platform.claude.com/settings/api-keys)

2. Purge stale sessions just in case

```bash
claude logout
```

3. Set API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

4. Always run inside the repo

```bash
cd ai-education-lab
```

5. Verify environment

```bash
bash tools/claude/check_env.sh
claude
```

6. Install the VSCode Extension

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

7. Confirm the integrated terminal works

In VSCode's integrated terminal (`Ctrl+\``):

```bash
claude -p "say hello" 
```

You should see an example response as below. The CLI and the extension share the same
authentication and settings.

```bash
Hello! How can I help you today?
```

8. Constrain scope in prompts

Always include:

"Only read files in this project directory. Do not access external folders."

9. Avoid large directories

Never run on:
* ~/
* Downloads/
* node_modules/

10. Kill runaway processes

Press:

* Ctrl + C (Windows/Linux)
* Cmd + . (Mac)

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

- NEVER commit API keys to GitHub
- DO NOT store keys in any tracked file
- Use environment variables only:
  - macOS/Linux: `export ANTHROPIC_API_KEY=...`
  - Windows: `setx ANTHROPIC_API_KEY ...`

If a key is leaked:
- Revoke immediately
- Generate a new key

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../provider_cost_control.md#pay-per-use)

## Documentation

[Claude Code (CLI)](https://code.claude.com/docs)
