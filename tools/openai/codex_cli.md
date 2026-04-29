# OpenAI Codex CLI Setup

## Install codex

Run in terminal:

```bash
npm install -g @openai/codex
```

Restart terminal after install.

## 🧭 API Setup

### 1. Set API key:

```bash
export OPENAI_API_KEY=...
```

### 2. Ensure fresh login session:

```bash
codex logout
printenv OPENAI_API_KEY | codex login --with-api-key
codex login status # verify login
```

### 3. Always run inside the repo

```bash
cd ai-education-lab
```

### 4. Verify environment


```bash
bash tools/openai/check_env.sh
```

### 5. Constrain scope in prompts

Always include:

"Only read files in this project directory. Do not access external folders."

### 6. Avoid large directories

Never run on:

* ~/
* Downloads/
* node_modules/

### 7. Kill runaway processes

Press:

* Ctrl + C (Windows/Linux)
* Cmd + . (Mac)

---

## 🔐 Security: API Keys

- NEVER commit API keys to GitHub
- DO NOT store keys in any tracked file
- Use environment variables only:
  - macOS/Linux: `export OPENAI_API_KEY=...`
  - Windows: `setx OPENAI_API_KEY ...`

If a key is leaked:
- Revoke immediately
- Generate a new key

---

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../dev_workbench/provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../dev_workbench/provider_cost_control.md#pay-per-use)
