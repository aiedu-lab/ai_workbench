# Multi-Model Tool Setup

## Install OpenAI Python Library

The `openai` Python library works with any OpenAI-compatible
provider (Groq, OpenRouter, Ollama, etc.) via a `base_url` swap.

```bash
pip install --upgrade pip
pip install openai
```

---

## Validation

### Groq API

Ensure `GROQ_API_KEY` is set, then verify the API responds:

```bash
python3 - <<'EOF'
import os
from openai import OpenAI
client = OpenAI(
  base_url="https://api.groq.com/openai/v1",
  api_key=os.environ["GROQ_API_KEY"]
)
resp = client.chat.completions.create(
  model="llama-3.1-8b-instant",
  messages=[{"role": "user", "content": "ping"}]
)
print(resp.choices[0].message.content)
EOF
```

Expected: a short reply from a Groq-hosted Llama model.

### OpenRouter API

Ensure `OPENROUTER_API_KEY` is set, then verify the API responds:

```bash
python3 - <<'EOF'
import os
from openai import OpenAI
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"]
)
resp = client.chat.completions.create(
  model="meta-llama/llama-3.1-8b-instruct:free",
  messages=[{"role": "user", "content": "ping"}]
)
print(resp.choices[0].message.content)
EOF
```

Expected: a short reply from OpenRouter.

### Cline VSCode Extension

1. Open VSCode extensions panel (`Ctrl+Shift+X`).
2. Verify **Cline** is installed and active (visible in the
   Activity Bar).
3. Open the Cline panel and confirm your OpenRouter API key
   is configured under Cline settings.
