# Speed Reading — Vibe Agenting

**Vibe Agenting**: the coordinator LLM dynamically decides
everything at runtime — how many subagents to create, what
function each one performs, and when to spawn them. There are
no pre-declared agent specs. You trigger it with a high-level
prompt and let the assistant invent specialists on the fly.

---

## File Layout

```
vibe/
  ai-mindmap.md       ← global mindmap doctrine
  speed-reading.md    ← speed-reading system description
  templates/
    mindmap-content.template.json
    mindmap-layout.template.json
    detailed-notes.template.md
  examples/
    contents/         ← source materials (gitignored)
    .tmp/             ← intermediate artifacts (gitignored)
```

---

## Single-Prompt Exercise

Open Claude CLI inside `vibe/`, grant full permissions
(`/permissions`), then:

```text
Study the contents of the current directory.
Study the book in the examples/ subdirectory.
Build a mindmap in the examples/ directory, descending
to layer 1 only.
Use subagents as appropriate.
```

The assistant invents its own subagents, routes work between
them, and produces a mindmap HTML in `examples/`.

To drill into a specific node after the level-1 run:

```text
Descend into layer 2 for the node <name>.
```

See the full exercise in
[`sessions/llm_wiki.md — Vibe Agenting Exercise`](
../../../../sessions/llm_wiki.md#vibe-agenting-exercise).