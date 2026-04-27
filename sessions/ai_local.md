# Concept & Exercise: AI Local (The Sovereign Developer)

## 🎯 Objective
Run a high-performance Large Language Model (LLM) entirely on your local hardware. You will learn how to bypass the cloud for ultimate privacy and create a "Custom Persona" tailored for specific academic fields.

---

## 🛠️ Phase 1: Preparation & Setup
Before beginning this exercise, you must ensure your computer has the hardware capacity to run an AI model, and you must install the engine.

👉 **[Go to the Local AI Setup Guide](../tools/ollama/setup.md)** and complete the installation for your specific operating system (Mac or Windows). Return here once you have successfully pulled your model.

---

## 👨‍🏫 Phase 2: The Socratic Physics Tutor Exercise
Generic AI easily becomes a "homework cheating machine." We are going to build a **Custom Model** that acts as a world-class Physics teacher who never gives the answer directly, but guides the student using the Socratic method.

### 1. Creating the Modelfile
In your project directory, create a file named `Modelfile` (no file extension). Paste the following:

    FROM llama3:8b 
    # (Note: Change the line above to gemma:2b if you downloaded the smaller model)

    # Lower temperature = more factual, less "hallucinated" creative drift
    PARAMETER temperature 0.3

    SYSTEM """
    You are 'Professor Newton', a high school Physics and Calculus tutor. 
    1. NEVER give the final numerical answer to a problem immediately.
    2. Always start by asking the student what physical laws (like Newton's 2nd Law) apply to the situation.
    3. Use relatable analogies (like sports or cars) to explain abstract forces.
    4. If the student is stuck, provide a 'hint' in the form of a simplified equation.
    5. Tone: Encouraging, curious, and slightly eccentric.
    """

### 2. Building your Agent
Open your terminal (PowerShell or Mac Terminal). Navigate to the folder where you saved the `Modelfile` and run:
```bash
ollama create prof-newton -f Modelfile
```

### 3. The Offline Interaction
**Turn off your laptop's Wi-Fi.** Run your new custom agent:
```bash
ollama run prof-newton
```
**Try this prompt:** *"I don't understand why a heavier bowling ball doesn't fall faster than a light tennis ball if gravity is pulling the heavy one harder."*

Observe how the AI responds without an internet connection, strictly following the pedagogical rules you established.

---

## 🔗 Stretch Goal — Connect to the Main Project

Ask Professor Newton (or your own custom agent) a question that
connects AI Local to the Group Meetup Organizer project arc:

```text
Explain the Poller → Selector → Notifier pattern used in a
Group Meetup Organizer system. Treat me like a student who
has just learned about Python functions for the first time.
```

Observe that the local model answers entirely offline — the same
architectural concept taught throughout the lab, now explained by
an AI you built yourself, running on your own hardware.

---

## 🔢 Stretch Goal B — Semantic Similarity with Local Embeddings

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Run this 5-line demo (requires only `ollama` and `numpy`):

```python
import ollama, numpy as np

def embed(text):
  return ollama.embeddings(
    model="nomic-embed-text", prompt=text
  )["embedding"]

a, b, c = map(np.array, [
  embed("The meeting is at 3pm"),
  embed("What time is my next event?"),
  embed("I enjoy hiking on weekends"),
])
def cosine(x, y):
  return float(
    np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
  )
print(f"related:   {cosine(a, b):.2f}")   # ~0.6–0.8
print(f"unrelated: {cosine(a, c):.2f}")   # ~0.1–0.2
```

> This is the same cosine similarity from
> [Advanced Prompting — §8](prompting_advanced.md#embeddings--retrieval-augmented-generation-rag),
> but running entirely offline. How does local embedding quality
> compare to the cloud model you used there?

---

## 🧹 Phase 3: Tear Down & Resource Recovery
Local AI consumes significant RAM while active. To "clean up" your workbench so your other apps don't lag:

1. **Exit the Chat:** Type `/bye`.
2. **Unload from RAM:** Ollama keeps models in memory for 5 minutes after use. To force-release your RAM immediately:
   ```bash
   ollama stop prof-newton
   ```
*(Note: The model files stay on your hard drive. They don't consume RAM when not running, so you can leave them there for the next lab session.)*
