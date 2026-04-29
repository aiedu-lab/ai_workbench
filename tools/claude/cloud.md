# Claude Cloud Setup

Every student needs a claude.ai account before using any Claude
tool (Desktop, CLI, or API). Complete this guide once; all other
tools cross-reference it.

---

## 1. Sign Up

1. Open [claude.ai](https://claude.ai) in your browser.
2. Click **Get started** and create an account using your Google
   account or email address.
3. Verify your email if prompted.
4. Choose the **Free** tier to start — upgrade to Pro if needed
   for higher usage limits or access to Claude Desktop features.

**Validation:** You can open a new conversation in the browser and
receive a response from Claude.

---

## 2. Generate an API Key

Required for: Claude Code CLI (`--api-key` mode), direct API calls,
and any Python/Node code that uses the Anthropic SDK.

1. Go to [platform.claude.com](https://platform.claude.com/).
2. Sign in with the same account you created above.
3. Navigate to **Settings → API Keys → Create Key**.
4. Name the key (e.g. `ai-lab-key`) and copy it — it is shown
   only once.

> **Do NOT share or commit your API key.** If it is ever exposed,
> revoke it immediately at `platform.claude.com/settings/api-keys`
> and generate a new one.

**Purchase credits (required for API use):**

Billing → Add credits → minimum $5. Without credits, API calls
return a 429 error.

---

## 3. Save the API Key as an Environment Variable

Set `ANTHROPIC_API_KEY` in your shell so every tool can find it
without hardcoding.

**macOS / Linux / WSL2:**

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
# To persist across terminal sessions:
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

**Validation:**

```bash
echo $ANTHROPIC_API_KEY        # must print your key (not empty)
```

> **NEVER** add this key to any file that is committed to Git.
> Add `.env` to `.gitignore` if you store keys in a local `.env`
> file.

---

## 4. Privacy Settings

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

## 5. Validate End-to-End

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

---

## Next Steps

| Tool | Setup guide |
|------|-------------|
| Claude Code CLI | [cli.md](cli.md) |
| Claude Desktop (Chat + CoWork) | [desktop.md](desktop.md) |
