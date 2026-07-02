# Speed Reading — Static Agenting

**Static Agenting**: agent functions are declared in markdown spec
files (`agents/*.md`). Unlike Dynamic Agenting, the dispatch
order, retry logic, lifecycle management, and observability are
all fixed in developer-written imperative code (`src/piper.py`
and `src/orchestrator.py`). The LLM does not route — the code
does.

This gives deterministic, traceable execution at the cost of
hand-rolled orchestration that must be maintained manually as the
pipeline evolves.

---

## File Layout

```
static/
  src/
    piper.py          CLI entry point; argument parsing
    orchestrator.py   Piper class; five pipeline phases
    display.py        Waterfall renderer
    spinner.py        Animated stderr progress indicator
  agents/
    seth-content-synthesizer.md
    leo-layout-engineer.md
    quinn-qa-reviewer.md
    sentinel-final-guardian.md
    piper-pipeline-orchestrator.md  ← doctrine (not a prompt)
  templates/
    mindmap-content.template.json
    mindmap-layout.template.json
    detailed-notes.template.md
  examples/
    contents/   ← source materials (gitignored)
    .tmp/       ← intermediate artifacts (gitignored)
```

---

## Quick-Start Exercise

```bash
cd projects/llm_wiki/speed-reading/static

# Show all options (including --level and --from-node)
python3 src/piper.py --help

# Build a level-1 mindmap only (fast — recommended for the exercise)
python3 src/piper.py \
  --input  examples/the-coming-wave.pdf \
  --output examples/the-coming-wave-mindmap.html \
  --level  1

# Monitor Leo in a second terminal
tail -f examples/.tmp/the-coming-wave-leo-1.log
```

`--level 1` tells both Seth and Leo to descend only one level
deep (root children only), completing the exercise in a fraction
of the time a full run would take.

To drill into one node after the level-1 run:

```bash
python3 src/piper.py \
  --input     examples/the-coming-wave.pdf \
  --output    examples/the-coming-wave-mindmap.html \
  --from-node "The Coming Wave" \
  --level     2
```

See the full exercise in
[`sessions/llm_wiki.md — Static Agenting Exercise`](
../../../../sessions/llm_wiki.md#static-agenting-exercise).

---

## Full Documentation

See [`../README.md`](../README.md) for the complete pipeline
overview, waterfall view, resume flags, and debug guide.
