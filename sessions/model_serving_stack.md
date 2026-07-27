# Concept: Model Serving Stack

## 🎯 Objective
Understand the layers between "you type a prompt" and "a model
predicts the next token": the agent harness, the model provider,
the foundation model itself, and the execution runtime that lets
the agent act on your files and tools. This layered view explains
why you can swap Claude for Llama without rewriting your workflow,
and what you gain or give up by running models locally instead of
in the cloud.

## 🧠 The Four Layers

```text
           Agent Harness
    (Aider, OpenCode, Gemini CLI,
     Claude Code, Codex)
                 │
         Model Provider Layer
(OpenAI, Anthropic, Google, Ollama,
 OpenRouter, Groq, LM Studio)
                 │
          Foundation Model
(GPT-5.x, Claude, Gemini, Qwen,
 DeepSeek, Llama, Mistral)
                 │
      Execution Runtime / Tools
(MCP, shell, git, Docker,
 Firecracker, gVisor, browser)
```

* **Agent Harness** — plans tasks, edits files, decides what to do
  next.
* **Model Provider** — routes your prompt to a hosted or local
  model and returns tokens.
* **Foundation Model** — the weights that actually predict the
  next token.
* **Execution Runtime** — the shell, git, Docker, or browser tools
  the agent is allowed to call.

## 🏗️ Three Ways to Assemble the Stack

### Commercial Integrated Products
Polished, all-in-one experiences (Claude Code, Claude Desktop,
Codex CLI, Cursor, Windsurf) that bundle harness + provider + model
and intentionally lock you into one ecosystem.

### Free Agent CLIs
Open or generously-free harnesses (Gemini CLI, Aider, OpenCode)
that work with almost any provider — GPT, Claude, Gemini, DeepSeek,
Ollama — so you pay only for the model, or nothing at all.

### Local Model Server (Ollama)
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

## ⚖️ Why Local-First Stacks

| | Local (Ollama) | Cloud (Claude, GPT, Gemini) |
|---|---|---|
| Cost | $0/month after hardware | Pay per token |
| Privacy | Fully offline | Data leaves your machine |
| Model strength | Weaker, open-weight | Frontier-grade |
| Speed | GPU-bound, can be slow | Fast, provider-managed |

## 🔑 Key Takeaway
The harness, the provider, and the model are three independent,
swappable layers — not one product. Picking a commercial
all-in-one tool trades flexibility for polish; picking a free
harness over Ollama or a cloud provider trades model strength and
speed for cost and privacy. Know which layer you're changing
before you "swap models."

## References
* [Best Codex CLI Alternatives (2026) – Tembo](
    https://www.tembo.io/blog/codex-cli-alternatives
  )
* [The best free CLI coding agents in 2026 – Freebuff](
    https://freebuff.com/blog/best-free-cli-coding-agents-2026
  )
* [Google is bringing Gemini CLI to developers' terminals –
  The Verge](
    https://www.theverge.com/news/692517/google-gemini-cli-ai-agent-dev-terminal
  )
