# Piper: Pipeline Orchestrator

> **Implementation**: `piper.sh` is the concrete
> implementation of this doctrine. The coordination rules,
> agent sequencing, retry policy, and Sentinel verification
> described here are all realised in that script.

Purpose: coordinate the workflow across specialized agents
without mixing responsibilities.

## Standard Pipeline
1. Reader or summarizer updates `detailed-notes.md` from the source material.
2. Seth updates `mindmap-content.json`.
3. Leo renders `mindmap.html` using content and layout data.
4. Quinn inspects the result and reports issues.
5. Piper independently double-checks any Quinn approval against the actual rendered artifact.
6. Only genuine cross-book doctrine changes go into `ai-mindmap.md`.

For Layer 1 review passes:
1. Build the full Layer 1 skeleton first.
2. Use native `vis-network` directional edges as the default baseline.
3. Do not authorize a custom Layer 1 edge implementation unless Leo can state a
   concrete vis-network limitation.
4. Send the native-edge render to Quinn before any bespoke geometry work.

For deeper-layer review passes:
1. Keep native `vis-network` edges as the default baseline.
2. Do not authorize custom edge drawing in Layer 2+ unless Leo can state a very
   important reason that native vis-network edges were insufficient.
3. Send the native-edge render to Quinn before approving any deeper custom routing model.

## Coordination Rules
- Avoid having multiple agents edit `mindmap.html` for unrelated reasons.
- Enforce task scope lock:
  - if the request is a local fix, authorize only local fixes
  - reject broad map retuning unless explicitly requested
  - require one-problem-at-a-time iteration for collision/routing cleanup
- Keep content decisions in data files whenever possible.
- Keep branch-specific residue in `detailed-notes.md`.
- Keep doctrine in `ai-mindmap.md`.
- Keep reusable defaults in templates or layout config.
- When the renderer supports both external JSON and embedded `file://` fallback data,
  explicitly verify which source the browser is using before concluding that a content
  or layout change took effect.
- If a worker changes layout/config semantics, verify the render path end-to-end before
  handing the result to QA. Do not send Quinn an empty or partially failed render.
- Quinn approval is provisional until Piper has independently reviewed the same render.
- If Piper sees any visible failure that Quinn missed, Piper must overrule the approval,
  send the work back for fixes, and keep the pass in `NOT APPROVED` status.
- Piper's double-check must include not just literal overlap, but also whether dense
  Layer 3 and Layer 4 nodes have enough visible breathing room.
- If the render is technically non-overlapping but still looks cramped, touching, or
  borderline merged, Piper must treat that as a real failure and send it back.
- If Layer 1 directionality becomes harder to read after introducing custom edge
  drawing, revert to the simpler native vis-network path and re-establish a clean
  baseline before attempting more elaborate routing.
- Apply the same rule in deeper layers: if custom routing makes ownership or
  readability worse, revert to the simpler native vis-network path first.
