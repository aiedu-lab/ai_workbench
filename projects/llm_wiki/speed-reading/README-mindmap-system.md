# Mind Map System

This directory stores reusable doctrine, agent instructions, and templates for building book mind maps.

## Files

### Active Agent Prompts (used by `src/piper.py`)
- `agents/seth-content-synthesizer.md`: Seth — distils book
  notes into structured mindmap JSON.
- `agents/leo-layout-engineer.md`: Leo — renders JSON into a
  self-contained HTML mindmap.
- `agents/quinn-qa-reviewer.md`: Quinn — QA-reviews the
  rendered HTML; outputs NOT APPROVED with failures.
- `agents/sentinel-final-guardian.md`: Sentinel — final
  independent verification; overrules Quinn approval if any
  layout, hierarchy, or rendering failure is present.

### Reference / Doctrine (not used as agent prompts)
- `ai-mindmap.md`: global doctrine and non-negotiable map
  rules.
- `agents/piper-pipeline-orchestrator.md`: Piper pipeline
  doctrine — multi-agent coordination rules, layer policies,
  task scope locking. Referenced when extending the pipeline
  or debugging coordination issues. The bash orchestrator
  (`src/piper.py`) implements this doctrine.

### Templates
- `templates/mindmap-content.template.json`: starter content
  schema
- `templates/mindmap-layout.template.json`: starter layout
  schema
- `templates/detailed-notes.template.md`: starter chapter-
  notes file

## Recommended Per-Book Files
All intermediate files are prefixed with the book name and
written to `<output-dir>/.tmp/` by `src/piper.py`:
- `<book>-detailed-notes.md`
- `<book>-mindmap-content.json`
- `<book>-mindmap.html`

## Depth Policy
- Layer 2 to Layer 4 are the normal working depths.
- Layers 5 and 6 are supported, but should be rare and strongly justified.
- If deeper content is mostly residue, examples, or chapter-local detail, prefer `detailed-notes.md` over extra map depth.

## Recommended Workflow
1. Fill `detailed-notes.md` from the book.
2. Distill concepts into `mindmap-content.json`.
3. Render Layer 1 first with `mindmap.html` using the content and layout files.
4. Use native `vis-network` edges as the default Layer 1 directionality path.
5. Use native `vis-network` edges as the default in deeper layers too.
6. Only introduce custom edge drawing after a demonstrated `vis-network` limitation
   or another very important reason.
7. Have Quinn review the rendered result.
8. Have Sentinel independently verify Quinn's approval —
   Sentinel overrules if it finds any failure Quinn missed,
   including cramped nodes or subtle layout defects.
9. Review screenshots and iterate.
10. Promote only genuine new doctrine into `ai-mindmap.md`.

### Scoped Fix Policy
- If a request targets one node/edge/local defect, treat it as a scoped repair.
- Apply the smallest local change first; avoid global retuning.
- Fix one problem at a time and validate before touching unrelated regions.
