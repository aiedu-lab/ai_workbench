# Claude CLI

## CLI Setup

Run in terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Restart terminal after install.

## 🧭 API Setup

### 1. Set API key:

```bash
export ANTHROPIC_API_KEY=...
```

### 2. Ensure no login session:

```bash
claude logout
```

### 3. Always run inside the repo

```bash
cd ai-education-lab
```

### 4. Verify environment


```bash
bash tools/claude/check_env.sh
claude
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
  - macOS/Linux: `export ANTHROPIC_API_KEY=...`
  - Windows: `setx ANTHROPIC_API_KEY ...`

If a key is leaked:
- Revoke immediately
- Generate a new key

---

## ⚠️ Guardrails

- Never run Claude on root directories
- Always constrain file scope (e.g., `src/`)
- Use a **Kill Switch** (`Ctrl + C`) for runaway agents
- Set API spend limits (e.g., $5)

---

## 💰 Tokenomics (Cost Awareness)

Two modes:
- **Subscription (Netflix)** → easy, less control
- **API (AWS)** → pay-per-use, precise, recommended for CLI