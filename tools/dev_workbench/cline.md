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

2. **Link Cline to LLM**
Cline can link to LLM Provider in two modes - `Direct` or `OpenRouter`:
- `Direct`:
   - **Configure VSCode -> Cline Settings Icon -> API Configuration:**
   - Click the Cline icon in the Activity Bar.
   - Settings (gear icon) → API Provider: say **OpenAI**
   - Paste your LLM Provider Key `OPENAI_API_KEY`.
   - Model: `gpt-5.4-mini`
   (low end tier; swap for a stronger model as needed).
   - **Save** the settings.
   - To qualify working setup reference [Validation](#validation)

- `OpenRouter`: OpenRouter can be linked in two modes - `Umbrella` or `BYOK`:
   - `Umbrella` Mode: OpenRouter is seen as the umbrella LLM provider 
      and solo billing entitiy. Behind the scenes, OpenRouter links 
      to multiple LLM providers but you see OpenRouter as the solo 
      LLM provider and billed as such.
      - **Configure [OpenRouter](https://openrouter.ai/) Key:**
         - Click on `Get API Key` -> `New Key`
         - Set Name, Expiration, Credit limit, Reset limit; leave BYOK blank
      - **Configure VSCode -> Cline Settings Icon -> API Configuration**:
      - Click the Cline icon in the Activity Bar.
      - Settings (gear icon) → API Provider: **OpenRouter**
      - Paste your `OPENROUTER_API_KEY`.
      - Model: `meta-llama/llama-3.1-8b-instruct:free`
      (free tier; swap for a stronger model as needed).
      - To qualify working setup reference [Validation](#validation)

   - `BYOK` Mode - Bring your own key - where you see an LLM provider,
      say OpenAI as your LLM provider and are billed by OpenAI as such. 
      One just uses OpenRouter as the LLM Gateway - URL endpoint.
      Click on [`BYOK`](https://openrouter.ai/workspaces/default/byok)
      where you choose one of the LLM provider in the backend of
      OpenRouter and add the `API Key` (eg `OPENAI_API_KEY`) that you 
      had provisioned directly at the corresponding LLM provider's website. 
      - **Configure [OpenRouter](https://openrouter.ai/) Key:**
         - Click on `Get API Key` -> `New Key`
         - Set Name; BYOK enabled; leave Expiration, Credit limit, Reset limit blank
      - **Configure VSCode -> Cline Settings Icon -> API Configuration**:
      - Click the Cline icon in the Activity Bar.
      - Settings (gear icon) → API Provider: **OpenRouter**
      - Paste your `OPENROUTER_API_KEY`.
      - Model: `gpt-5.4-mini`
      (low end tier; swap for a stronger model as needed).
      - To qualify working setup reference [Validation](#validation)

---

## Validation

For each of the above cases: in the Cline panel, send:

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
