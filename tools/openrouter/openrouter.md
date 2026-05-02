# OpenRouter

OpenRouter is a unified API gateway that routes requests to
100+ models (GPT-4o, Claude, Llama, Gemini, Qwen, etc.)
through a single OpenAI-compatible endpoint. Useful for
comparing models and accessing free open-weight models.

---

## Setup

1. **Create an account** at
   [openrouter.ai](https://openrouter.ai/) → Sign Up.

2. **Generate an API key:**
   Dashboard → API Keys → Create Key
   → copy the key immediately.

3. **Save the key as an environment variable** inside Ubuntu:

```bash
echo 'export OPENROUTER_API_KEY="<paste-your-key>"' >> ~/.bashrc
source ~/.bashrc
```

4. **BYOK (Bring Your Own Key):** OpenRouter supports routing
   through your own Anthropic / OpenAI keys to avoid markup.
   Dashboard → Integrations → add your provider key.

---

## Validation

Confirm the key works:

```bash
pip install openai   # OpenRouter uses the OpenAI SDK
python3 -c "
from openai import OpenAI
client = OpenAI(
  base_url='https://openrouter.ai/api/v1',
  api_key='$OPENROUTER_API_KEY'
)
resp = client.chat.completions.create(
  model='meta-llama/llama-3.1-8b-instruct:free',
  messages=[{'role':'user','content':'say hello'}]
)
print(resp.choices[0].message.content)
"
```

Expected: a greeting from Llama 3.1 (or whatever free
model OpenRouter selects).

Check activity and cost:

```bash
# Or open the dashboard
open https://openrouter.ai/activity
```

---

## Tracking Token Usage

- [openrouter.ai/activity](https://openrouter.ai/activity)
  shows requests, tokens used, and cost per call.
- Free models are labelled `:free` — $0.00 cost.

---

## Comparison: Provider Dashboards

| Provider | Usage Dashboard |
|---|---|
| Anthropic | platform.claude.com → Analytics |
| OpenAI | platform.openai.com/usage |
| Gemini | Google Cloud Console → Billing |
| OpenRouter | openrouter.ai/activity |
