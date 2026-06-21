# Applications on Pluggable Models

<!-- AI-GENERATED: Phase 17 Step 17.7
     (miscellaneous/software_defined_workbench/plan.md) -->

Learn to build AI-powered apps where the "brain" (LLM) is a
pluggable component — swap providers without changing your
application code.

---

## Concept

### Closed vs Open-Weight Models

| Dimension | Closed | Open-Weight |
|---|---|---|
| Who runs it | Provider cloud | Anyone |
| Weights shared | No | Yes |
| Examples | Claude, GPT-4o | Llama, Qwen, Mistral |
| Cost | API pricing | Free (compute only) |
| Privacy | Data sent to provider | Runs locally or on own infra |

### The OpenAI-Compatible API Standard

Most LLM providers (Groq, OpenRouter, Ollama, Together AI)
implement the same REST interface that OpenAI introduced.
One Python library — `openai` — works with all of them
via a `base_url` swap:

```python
# Groq
client = OpenAI(
  base_url="https://api.groq.com/openai/v1",
  api_key=os.environ["GROQ_API_KEY"]
)

# OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ["OPENROUTER_API_KEY"]
)
```

Only two variables change. Your application code is identical.

---

## Tools

| Tool | Purpose | Setup |
|---|---|---|
| Groq | Ultra-fast LPU inference | [miscellaneous/tools/groq/setup.md](../miscellaneous/tools/groq/setup.md) |
| OpenRouter | Gateway to 100+ models | [miscellaneous/tools/openrouter/openrouter.md](../miscellaneous/tools/openrouter/openrouter.md) |
| Cline | VSCode AI assistant | [miscellaneous/tools/dev_workbench/cline.md](../miscellaneous/tools/dev_workbench/cline.md) |

---

## Setup

Install the OpenAI Python library (works with any provider) — see
[Install OpenAI Python Library](
../miscellaneous/tools/dev_workbench/multimodel.md
#install-openai-python-library).

Set your API keys:
- **Groq:** see [Groq Setup](../miscellaneous/tools/groq/setup.md)
- **OpenRouter:** see
  [OpenRouter Setup](../miscellaneous/tools/openrouter/openrouter.md)

---

## Exercise: The Brain Swap Experiment

**Objective:** Build a provider-agnostic Python app and swap
the underlying LLM without changing your code.

### Phase 1: Environment Setup

1. Install dependencies — see
   [Install OpenAI Python Library](
   ../miscellaneous/tools/dev_workbench/multimodel.md
   #install-openai-python-library).

2. Get API keys from the Tool Setup guides above.

### Phase 2: The Code

Create `hello_ai.py`. This skeleton works with any provider:

```python
import os
from openai import OpenAI

# --- CONFIGURATION — change only these two lines to swap ---

# Option A: Groq (ultra-fast LPUs)
# URL = "https://api.groq.com/openai/v1"
# KEY = os.environ["GROQ_API_KEY"]
# MODEL = "llama-3.1-8b-instant"

# Option B: OpenRouter (free open-weight models)
URL = "https://openrouter.ai/api/v1"
KEY = os.environ["OPENROUTER_API_KEY"]
MODEL = "meta-llama/llama-3.1-8b-instruct:free"

# -----------------------------------------------------------

client = OpenAI(base_url=URL, api_key=KEY)


def ask_ai(prompt):
  print(f"\n[Sending to {MODEL}...]")
  resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}]
  )
  return resp.choices[0].message.content


user_prompt = (
  "Write a 3-line Python script that prints "
  "'Hello World' and the current time."
)
print("AI Response:", ask_ai(user_prompt))
```

### Phase 3: Lab Tasks

**Task 1 — Hello World test:**

```bash
python3 hello_ai.py
```

Observe: how long did it take? Which model ran?

**Task 2 — Brain Swap:**

Comment out Option B lines. Uncomment Option A (Groq).
Replace the API key placeholder and run again.

Observe: did speed change? Groq's LPUs are often 10× faster.

**Task 3 — Identity Check:**

Change `user_prompt` to:

```text
Who are you, and what is your architecture?
```

Observe: open-weight models (Llama, Qwen) name their version.
Closed models often say "I am a large language model."

### Phase 4: Critical Thinking

1. **Portability:** Why use the `openai` library even when
   you aren't using OpenAI's models?

2. **Economics:** Check your Groq or OpenRouter dashboard.
   What did this lab cost? (Usually $0.00.)

3. **Resilience:** If a provider went offline tomorrow,
   could you still run `hello_ai.py`?
   Hint: research **Ollama** and the
   [AI Local session](ai_local.md).

---

## Reflection

- Which model responded fastest? Which gave the best answer?
- What would break in `hello_ai.py` if providers did NOT share
  a common API standard?
- Where in the Group Meetup Organizer could you swap the model
  to reduce cost or improve speed?

---

## Output

- `hello_ai.py` committed to your personal branch.
- At least two providers tested (Groq + OpenRouter).
- Notes on speed, quality, and cost differences.
