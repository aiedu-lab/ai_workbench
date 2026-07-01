# Speed Reading — Dynamic Agenting

**Dynamic Agenting**: agent functions are pre-declared in markdown
spec files. The coordinator LLM reads those specs, discovers the
specialists, and decides which ones to invoke and in what order.
Routing is **LLM-driven** — the coordinator acts as an autonomous
orchestrator, not a fixed script.

The platform manages per-agent traces, token accounting, and
scoped permission boundaries declaratively through the harness.

---

## File Layout

```
dynamic/
  ai-mindmap.md       ← global mindmap doctrine
  speed-reading.md    ← speed-reading system description
  templates/
    mindmap-content.template.json
    mindmap-layout.template.json
    detailed-notes.template.md
  examples/
    contents/         ← source materials (gitignored)
    .tmp/             ← intermediate artifacts (gitignored)
      agents/         ← agent specs created in pass 1
```

---

## Two-Pass Exercise

### Pass 1 — Create agent specs

Open Claude CLI inside `dynamic/`, grant full permissions
(`/permissions`), then prompt:

```text
Study the speed reading system in the current directory.

You be the Orchestrator agent.
Suggest what specialized subagents we create to do the work.
In addition, ensure you create a QA subagent to validate
the work.

Create an agents sub directory in examples/.tmp/ and make
md files for each subagent inside examples/.tmp/agents/.
```

The LLM will produce markdown spec files for each specialist
(synthesizer, renderer, QA, etc.) in `examples/.tmp/agents/`.

### Pass 2 — Produce the mindmap

Exit and reopen Claude CLI (fresh session), then prompt:

```text
Study the material in the current directory.
Read the book in the examples/ subdirectory.
Create subagents from the specs in examples/.tmp/agents/
while you be the orchestrator.
Produce a mindmap html in examples/.
Create intermediate artifacts (json, md, logs) in
examples/.tmp/.
Descend only into layer 1.
```

The LLM routes to its declared specialists, collects results,
and writes the mindmap HTML to `examples/`.

See the full exercise in
[`sessions/llm_wiki.md — Dynamic Agenting Exercise`](
../../../../sessions/llm_wiki.md#dynamic-agenting-exercise).
