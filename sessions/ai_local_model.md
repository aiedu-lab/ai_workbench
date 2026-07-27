# Concept: AI Local

## 🎯 Objective
Go one layer deeper than [Model Serving
Stack](model_serving_stack.md): which open-weight models you can
actually run on your own hardware, which agent harnesses know how
to drive them, and what Ollama is doing under the hood when it
serves one. This is the "how local really works" session — the
hands-on lab is [Exercise: AI Local](ai_local.md).

## 📦 Local Open-Weight Models
These are the model *weights* you download and run yourself —
no API key, no cloud account:

* **Llama** (Meta) — general-purpose, widely supported baseline.
* **Qwen** (Alibaba) — strong at coding tasks, several small sizes.
* **DeepSeek** — competitive reasoning and coding performance.
* **Mistral** — compact, fast, popular for laptop-class hardware.
* **Gemma** (Google) — lightweight, tuned for constrained memory.

Smaller sizes (2B–8B parameters) fit on a laptop CPU/GPU; larger
ones need real VRAM. Quantized versions trade a little accuracy
for a much smaller footprint.

## 🤖 Agent Harnesses for Local Models
An agent harness is what plans and edits — it needs to be told to
point at a local server instead of a cloud API:

### Aider
The most mature open-source coding agent.
* CLI-only, repository-aware, automatic git commits per change.
* Works with almost any model: GPT, Claude, Gemini, DeepSeek,
  Ollama, LM Studio.
* Cost: the agent itself is free — you only pay for the model (or
  run it locally for free).

### OpenCode
One of the fastest-growing open harnesses.
* CLI, Desktop, and IDE surfaces.
* 70+ providers supported, including Ollama and OpenRouter.
* MIT licensed; a very Claude-Code-like experience.

Both point at Ollama's local REST endpoint the same way they'd
point at any cloud provider — the harness code doesn't change,
only the URL and model name.

## Local Model Server

**Ollama**

### Local Model Serving Stack
```
Aider, OpenCode
      │
      ▼
  Ollama
      │
      ▼
  Llama 3, Qwen, Kimi, ...
```

### What Ollama does and what it does not

Runs entirely on your laptop. Ollama itself does not plan, edit
code, or manage git — it only:
1. finds and downloads a model from a registry, verifying it
2. loads it into RAM/GPU
3. starts inference and a local REST API (e.g.
   `http://localhost:11434`)
4. manages installed models (list, remove, swap)
5. supports quantized model formats to fit smaller hardware

Ollama does **not** provide planning, git workflows, autonomous
execution, code editing, memory, or subagents — an agent harness
(Aider, OpenCode) still does the planning; Ollama just serves the
model underneath it.


Functionalities offered by Ollama:

#### 1. local inference

* drives inference engine based on model weights - 
  feeds input tokens and gathers output tokens

#### 2. REST API  - tiny webserver for code to talk to the model

* starts tiny webserver eg. http://localhost:11434
* allows python code to talk to the model eg. POST /generate

```text
VS Code
  │
  Python
    │
    Web Server
    │
    Aider, Continue, OpenCode
      │
      │
      ▼
      Ollama API
        │
        ▼
        Llama model
```

#### 3. model management

* locates, removes, lists, etc. models - llama3, deepseek, 
  qwen, mistral, gemma

#### 4. downloads

* contacts registry
* downloads the model, verifies, and stores it 

#### 5. quantization

Supports and manages quantized models, namely:
* Download compatible quantized models
* Recognize different quantization formats
* Choose right runtime behavior for them

It does **not** provide

* planning
* git workflows
* autonomous execution
* code editing
* memory
* subagents

## ⚙️ How Ollama Serves a Model

Running `ollama run llama3` triggers a full pipeline behind one
command:

```text
You
 │  "Run Llama"
 ▼
Ollama
 ├── finds the model
 ├── downloads, verifies, and stores it
 ├── loads it into RAM
 ├── loads the GPU
 ├── manages memory
 ├── starts inference
 ├── starts a web server, serves the REST API
 ├── waits for questions
 └── returns answers
        │
        ▼
     Llama model
```

Models are passive files — they never download or load themselves.
Ollama is the active layer that contacts the registry, verifies
and stores the weights, and turns a static file into something
that answers questions over `POST /generate`.

## ⚖️ Why Local-First Stacks

| | Local (Ollama) | Cloud (Claude, GPT, Gemini) |
|---|---|---|
| Cost | $0/month after hardware | Pay per token |
| Privacy | Fully offline | Data leaves your machine |
| Model strength | Weaker, open-weight | Frontier-grade |
| Speed | GPU-bound, can be slow | Fast, provider-managed |

## 🔑 Key Takeaway
Local serving isn't just "download a model" — Ollama is a small
runtime that downloads, verifies, loads, and exposes the model as
an API, and any harness (Aider, OpenCode) that speaks that API can
drive it exactly like a cloud provider. The model, the server, and
the harness stay independently swappable.

## 🏃 Exercise
For the hands-on lab — pulling a model, building a custom Modelfile
persona, and running it fully offline — see
[Exercise: AI Local](ai_local.md).
