# Claude Cloud Account

Every student needs a claude.ai account before using any Claude
tool (Desktop, CLI, or API). Complete this guide once; all other
tools cross-reference it.

---

## 1. Sign Up

1. Open [claude.ai](https://claude.ai) in your browser.
2. Click **Get started** and create an account using your Google
   account or email address.
3. Verify your email if prompted.
4. Choose the **Pro** subscription — required for Claude Desktop,
   Claude Code CLI, and higher usage limits in the lab.

**Validation:** You can open a new conversation in the browser and
receive a response from Claude.

---

## 2. Privacy Settings

Opt out of data training and location sharing before using Claude
for any lab work.

1. Open [claude.ai](https://claude.ai) and click your **profile
   icon** (top-right).
2. Go to **Settings → Privacy**.
3. **Disable** both of the following:
   - *"Help improve Claude — Allow the use of your chats and coding
     sessions to train and improve Anthropic AI models."*
   - *"Allow Claude to use coarse location metadata (city/region)
     to improve product experiences."*
4. Save changes.

> These settings apply to the browser chat. Claude Code CLI and
> API calls are governed by the API Terms of Service, which already
> exclude training on API data.

---

## Disable Claude Connectors

Claude Connectors let claude.ai silently attach MCP servers to
every conversation, consuming context and token budget without
explanation. Disable them before using any lab tool.

1. Set the environment variable: `ENABLE_CLAUDEAI_MCP_SERVERS=false`.
2. Add it to `~/.bashrc` so it persists across sessions (the lab's
   dev container is Linux-based and always sources `~/.bashrc`).

**Validation:** `echo $ENABLE_CLAUDEAI_MCP_SERVERS` → expect
`false`.

---

## 3. Generate and save an API Key

Required for: Claude Code CLI (`--api-key` mode), direct API calls,
and any Python/Node code that uses the Anthropic SDK.

1. Go to [platform.claude.com](https://platform.claude.com/).
2. Sign in with the same account you created above.
3. Navigate to **Settings → API Keys → Create Key**.
4. Name the key (e.g. `ai-lab-key`) and copy it — it is shown
   only once.
5. Reference [set `ANTHROPIC_API_KEY` in environment variable](
   cli.md#api-key-mode) so every tool can find it without hardcoding.

> **Do NOT share or commit your API key.** If it is ever exposed,
> revoke it immediately at `platform.claude.com/settings/api-keys`
> and generate a new one.

**Purchase credits (required for API use):**

Billing → Add credits → choose minimum $5. Note we'll use API
pay-per-use only as an insurance to complete tasks when we 
exhaust subscription based token credit limits. Without credits, 
API calls return a 429 error.

---

## 4. Validate End-to-End

Confirm your account, key, and env var all work together:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-haiku-4-5-20251001",
    "max_tokens": 32,
    "messages": [{"role": "user", "content": "ping"}]
  }'
```

Expected: JSON response containing `"type": "message"` and a
short reply. Any `401` or `403` means the key is wrong or has
no credits.
