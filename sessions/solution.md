# Solution Architecture

## Objective

See how a real AI solution combines Predictive AI, Generative AI,
non-AI algorithms, and systems engineering — and understand why
removing any layer makes the system fail or become brittle.

---

## Tools

* [Claude Chat](../tools/claude/desktop.md) — for the generative layer
* Python — for the classifier call and routing logic
* Discord webhook — reused from the Group Meetup project

---

## Concept — Modern AI Solution Architecture (15 min)

| Layer | Role | Example |
|-------|------|---------|
| Predictive AI | Classify, rank, score | Spam classifier, intent detector |
| Generative AI | Draft, reason, decide | LLM writes the reply |
| Non-AI algorithms | Route, filter, enforce | Priority queue, regex guard |
| Systems engineering | Persist, deliver, scale | Database, API, containers |

None of these layers is optional in a real solution. Remove any
one and the system either fails or becomes brittle:

- **No Predictive AI:** the LLM spends tokens classifying spam it
  could have discarded in milliseconds for a fraction of the cost.
- **No Generative AI:** the system routes and delivers but produces
  no intelligent content — a pipeline with no brain.
- **No non-AI algorithms:** the LLM makes routing decisions it is
  not reliable enough to make consistently (urgency detection,
  compliance filtering).
- **No systems engineering:** results are never stored, delivered,
  or observable — the pipeline exists only in RAM.

---

## Visual Anchor — MNIST Demo (5 min)

A pre-trained digit classifier predicts handwritten digits from
pixels. This is Predictive AI at its simplest: pattern → label.

```python
# Run in Google Colab — no local install required
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import numpy as np

# Use a pre-trained Keras MNIST model (included in Colab examples)
# model = load_model("mnist_model.h5")
# prediction = model.predict(image.reshape(1, 28, 28, 1))
# print("Predicted digit:", np.argmax(prediction))
```

**Contrast:** Ask an LLM what digit it sees in the same image.
The LLM describes it; the classifier labels it.

| | Classifier | LLM |
|-|-----------|-----|
| Speed | Milliseconds | Seconds |
| Cost | Fractions of a cent | Cents to dollars |
| Scope | One narrow task | Any task |
| Failure mode | Confident wrong label | Hallucination |

A real system uses both: the classifier filters and routes
cheaply; the LLM reasons about what made it through the filter.

---

## Exercise — Email Triage System (25 min)

Build a four-layer pipeline that processes an incoming email.
Reuse the Group Meetup Discord webhook — no new infrastructure.

```
Email arrives
     |
     v
[Predictive: spam classifier] ── spam? → discard
     |
     v (not spam)
[Generative: LLM drafts reply]
     |
     v
[Non-AI: rule-based priority router]
  urgent? → send immediately
  normal? → queue for digest
  unclear? → flag for human
     |
     v
[Systems: Discord webhook — same one from Group Meetup project]
```

### Step 0 — Prerequisites

```bash
pip install requests transformers torch
export DISCORD_WEBHOOK_URL="<from instructor — same as Group Meetup>"
```

### Step 1 — Predictive Layer: Spam Classifier

Call the HuggingFace Inference API (free tier — one line, no GPU):

```python
import requests

HF_API = (
  "https://api-inference.huggingface.co/models/"
  "mrm8488/bert-tiny-finetuned-sms-spam-detection"
)

def classify_spam(text: str) -> bool:
  resp = requests.post(HF_API, json={"inputs": text})
  label = resp.json()[0][0]["label"]
  return label == "LABEL_1"  # LABEL_1 = spam
```

Test with:
```python
print(classify_spam("Win a free iPhone now!!!"))  # True
print(classify_spam("Can we meet Thursday at 7pm?"))  # False
```

### Step 2 — Generative Layer: LLM Draft

```python
import subprocess

def draft_reply(email: str) -> str:
  prompt = (
    f"Draft a short, professional reply to this email:\n\n{email}"
  )
  result = subprocess.run(
    ["claude", "-p", prompt],
    capture_output=True, text=True,
  )
  return result.stdout.strip()
```

### Step 3 — Non-AI Layer: Priority Router

```python
URGENT_KEYWORDS = ["urgent", "asap", "deadline", "emergency"]

def route(email: str) -> str:
  lower = email.lower()
  if any(k in lower for k in URGENT_KEYWORDS):
    return "urgent"
  if "?" in email or len(email) < 200:
    return "normal"
  return "unclear"
```

### Step 4 — Systems Layer: Discord Delivery

```python
import os

def notify(draft: str, priority: str) -> None:
  label = {
    "urgent": "🚨 **URGENT**",
    "normal": "📬 **New email**",
    "unclear": "🤔 **Needs human review**",
  }[priority]
  msg = f"{label}\n\n{draft}"
  requests.post(
    os.environ["DISCORD_WEBHOOK_URL"],
    json={"content": msg},
  )
```

### Step 5 — Wire the Pipeline

```python
def triage(email: str) -> None:
  if classify_spam(email):
    print("Discarded: spam")
    return
  draft = draft_reply(email)
  priority = route(email)
  if priority == "unclear":
    print("Flagged for human review — not sent")
    return
  notify(draft, priority)
  print(f"Sent to Discord as: {priority}")

# Test
triage("Win a free iPhone now!!!")
triage("Can we meet Thursday at 7pm?")
triage("URGENT: server is down, need fix ASAP")
```

### Validation

- [ ] `classify_spam("Win a free iPhone")` returns `True`
- [ ] `classify_spam("Can we meet Thursday?")` returns `False`
- [ ] `draft_reply(...)` returns a non-empty string
- [ ] `route("URGENT: fix ASAP")` returns `"urgent"`
- [ ] Discord `#meetup-notifications` receives the triage output
  for the non-spam, non-unclear email

---

## Reflection

- Which part would you replace with a generative model? Which
  should stay algorithmic, and why?
- What happens if the spam classifier is wrong 5% of the time?
  Which layer catches the error?
- Where in this pipeline would Temporal add the most value?

---

## Output

* [Notes](../learnings/session_notes/solution.md)
