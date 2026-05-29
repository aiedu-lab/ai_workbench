# Mind Map System

This directory stores reusable doctrine, agent instructions, and templates for building book mind maps.

## Files
- `ai-mindmap.md`: global doctrine and non-negotiable map rules
- `agents/seth-content-synthesizer.md`: Seth, the content synthesizer who derives and prunes concepts
- `agents/leo-layout-engineer.md`: Leo, the layout engineer who places and renders the map
- `agents/quinn-qa-reviewer.md`: Quinn, the QA reviewer who inspects the rendered result
- `agents/piper-pipeline-orchestrator.md`: Piper, the pipeline orchestrator who coordinates the workflow
- `templates/mindmap-content.template.json`: starter content schema
- `templates/mindmap-layout.template.json`: starter layout schema
- `templates/detailed-notes.template.md`: starter chapter-notes file

## Recommended Per-Book Files
- `mindmap-content.json`
- `mindmap-layout.json`
- `mindmap.html`
- `detailed-notes.md`

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
8. Have Piper independently double-check any Quinn approval against the same render,
   including breathing room between dense nodes, not just literal overlap.
9. Review screenshots and iterate.
10. Promote only genuine new doctrine into `ai-mindmap.md`.

### Scoped Fix Policy
- If a request targets one node/edge/local defect, treat it as a scoped repair.
- Apply the smallest local change first; avoid global retuning.
- Fix one problem at a time and validate before touching unrelated regions.
