# Groq

Groq provides ultra-fast LLM inference using its custom
**Language Processing Unit (LPU)** hardware. Ideal for
latency-sensitive tasks and free-tier experimentation.

---

## Setup

1. **Create an account** at
   [console.groq.com](https://console.groq.com/)
   → Sign Up → verify email.

2. **Generate an API key:**
   Console → API Keys → Create API Key
   → copy the key immediately (shown only once).

3. **Save the key as an environment variable** inside Ubuntu:

```bash
# Add to ~/.bashrc so it persists across sessions
echo 'export GROQ_API_KEY="<paste-your-key-here>"' >> ~/.bashrc
source ~/.bashrc
```

---

## Validation

Test the key with a minimal Python call:

```bash
pip install groq
python3 -c "
from groq import Groq
client = Groq()
resp = client.chat.completions.create(
  model='llama-3.1-8b-instant',
  messages=[{'role': 'user', 'content': 'say hello'}]
)
print(resp.choices[0].message.content)
"
```

Expected: a short greeting from the model.

Alternatively, confirm via `curl`:

```bash
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"llama-3.1-8b-instant",
       "messages":[{"role":"user","content":"say hello"}]}'
```

---

## Notes

- Free tier: generous rate limits for students.
- Dashboard: [console.groq.com](https://console.groq.com/)
  → Usage to track requests and tokens.
- Compatible with the OpenAI Python SDK (`base_url` swap).
