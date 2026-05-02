# Cline

Cline is an AI coding assistant VSCode extension that can
plan, write, and execute code using any OpenAI-compatible
model. Used here as a secondary agent when Claude is
rate-limited or when you need a second opinion.

---

## Setup

1. **Install Cline:**
   Extensions (`Ctrl+Shift+X`) → search "Cline" → Install
   **Cline** (saoudrizwan).

2. **Configure OpenRouter as the API provider:**
   - Click the Cline icon in the Activity Bar.
   - Settings (gear icon) → API Provider: **OpenRouter**
   - Paste your `OPENROUTER_API_KEY`.
   - Model: `meta-llama/llama-3.1-8b-instruct:free`
     (free tier; swap for a stronger model as needed).

3. **Save** the settings.

---

## Validation

In the Cline panel, send:

```text
Just act as a conversational assistant and say hello.
```

Expected: Cline responds with a greeting.
If it responds, setup is complete.

---

## Usage Model

| Tool | When to use |
|---|---|
| **Claude Code (Pro)** | Primary — planning, code generation, validation |
| **Cline + OpenRouter** | Secondary — cross-checking plans, code review, when Claude is rate-limited |

**Cost:** Free-tier OpenRouter models cost $0.00.
Monitor usage at [openrouter.ai/activity](https://openrouter.ai/activity).

---

## Tracking Token Usage

| Provider | Dashboard |
|---|---|
| Anthropic | platform.claude.com → Workspace → Analytics |
| OpenAI | platform.openai.com/usage |
| Gemini | Google Cloud Console → Billing |
| OpenRouter | openrouter.ai/activity |
