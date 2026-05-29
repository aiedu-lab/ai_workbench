# 🌐 AI Instructions for Building an HTML MindMap

The MindMap is an interactive HTML file using **vis-network**. Use
vis-network for node rendering, edge rendering, zoom, pan, and hit-testing.
Do **not** hand-draw the whole map with raw D3 or custom SVG unless there is a
clear renderer limitation that vis-network cannot handle.

The renderer should still behave like a curated radial mind map, not a generic
force graph. Compute the node positions yourself, then pass those fixed
positions into vis-network.

This is a **hard layout constraint**, not a preference:

- No edge may pass through any node except at its own endpoint.
- No edge may intersect another edge if a cleaner layout is possible.
- If the renderer cannot satisfy those constraints with the current placement,
  it must move nodes, widen sectors, increase local radius, or reroute the
  edge until the conflict is gone.

Nodes are clickable ovals; clicking shows a tooltip with both **"What is it?"**
and **"Why is it important?"**

## 📦 Self-contained operating contract

This file is designed to work as a **standalone companion** to
`speed-reading.md`. No other file in this directory is required in order to use
the method correctly.

Other files, if present, should be treated as optional helpers only:

- agent-specific instructions
- starter templates
- repo-local workflow notes

The minimum per-book working set is:

- `detailed-notes.md`
- `mindmap-content.json`
- `mindmap-layout.json`
- `mindmap.html`

If those files do not exist yet, create them from the starter contracts below.

## 🗂️ Minimal per-book workflow

Use this exact sequence unless there is a strong reason not to:

1. Read and prune into `detailed-notes.md`.
2. Distill durable anchors into `mindmap-content.json`.
3. Tune spacing and layout defaults in `mindmap-layout.json`.
4. Render `mindmap.html`.
5. Run geometry-aware validation.
6. Review the rendered artifact in a real browser.
7. If the map is crowded, transcript-like, or routing-dirty, consolidate the
   content first before expanding the layout.

## 🎯 Scope-locked fix protocol (non-negotiable)

When a task asks to fix a specific node, edge, or local collision, treat it as a
**scoped repair**, not a global retune.

- Change the smallest effective control first.
- Prefer local knobs in this order:
  - node-specific override
  - that node's parent-specific override
  - branch-local override
  - global defaults only as a last resort
- Fix **one reported problem at a time**. Do not bundle unrelated layout cleanups.
- After each scoped change, re-render and verify:
  - the targeted issue is resolved
  - no new unrelated regressions were introduced
- If a local tweak creates collateral regressions, revert that tweak and choose a
  narrower control.
- Do not rebalance the whole map unless the request explicitly asks for a global
  pass.

If multiple people or agents are involved, keep these roles separate:

- **Content synthesis**
  - decides what belongs in the map versus notes
- **Layout engineering**
  - places nodes, routes edges, and controls panel behavior
- **QA review**
  - inspects the rendered artifact for hierarchy and routing failures
- **Orchestration**
  - ensures the approved render is the actual current render path

## 📄 Starter file contracts

The following shapes are enough to start from scratch without any external
templates.

### `detailed-notes.md`

Use this file for chapter-specific residue that is helpful but not map-worthy.

```md
# Book Notes

This file stores chapter-specific detail that has been pruned from the map so
the mind map can keep only durable anchors.

## Chapter 1 - Title

- Add chapter-specific residue here.

## Chapter 2 - Title

- Add chapter-specific residue here.
```

### `mindmap-content.json`

This is the content source of truth. Every node needs:

- `id`
- `label`
- `what`
- `why`

Use stable IDs when refining an existing map.

```json
{
  "root": {
    "id": "root",
    "label": "Book Title",
    "what": "One-sentence description of the book's core idea.",
    "why": "Why this book matters as a whole."
  },
  "branches": [
    {
      "id": "b1",
      "label": "Branch One",
      "what": "Top-level branch summary.",
      "why": "Why this branch matters.",
      "emphasis": true
    }
  ],
  "layer2": [
    {
      "id": "m1",
      "branchId": "b1",
      "label": "Layer 2 Node",
      "what": "Durable concept.",
      "why": "Why it belongs at Layer 2.",
      "emphasis": false
    }
  ],
  "layer3": {
    "m1": [
      {
        "id": "m1-l3a",
        "label": "Layer 3 Node",
        "what": "Mechanism, tactic, or consequence.",
        "why": "Why this deeper node matters.",
        "emphasis": false
      }
    ]
  },
  "layer4": {
    "m1-l3a": [
      {
        "id": "m1-l4a1",
        "label": "Layer 4 Node",
        "what": "Optional deeper clarification.",
        "why": "Why this extra depth is worth keeping.",
        "emphasis": false
      }
    ]
  },
  "layer5": {
    "m1-l4a1": [
      {
        "id": "m1-l5a1",
        "label": "Layer 5 Node",
        "what": "Rare deeper clarification.",
        "why": "Why Layer 5 is justified instead of moving this to notes.",
        "emphasis": false
      }
    ]
  },
  "layer6": {
    "m1-l5a1": [
      {
        "id": "m1-l6a1",
        "label": "Layer 6 Node",
        "what": "Very rare deepest clarification.",
        "why": "Why Layer 6 is still map-worthy.",
        "emphasis": false
      }
    ]
  }
}
```

### `mindmap-layout.json`

These are starter layout knobs, not fixed truths.

```json
{
  "branchRing": {
    "rx": 980,
    "ry": 660,
    "startAngle": -1.57079632679,
    "margin": 0.18
  },
  "radii": {
    "layer2": 468,
    "layer3": 276,
    "layer4Base": 222,
    "layer5Base": 184,
    "layer6Base": 154
  },
  "stagger": {
    "layer2SiblingOffset": 34,
    "layer3AltOffsetInner": -12,
    "layer3AltOffsetOuter": 14,
    "layer4AltOffsetInner": -12,
    "layer4AltOffsetOuter": 20,
    "layer5AltOffsetInner": -10,
    "layer5AltOffsetOuter": 16,
    "layer6AltOffsetInner": -8,
    "layer6AltOffsetOuter": 12
  },
  "collision": {
    "layer3PushFactor": 0.6,
    "layer4PushFactor": 0.82,
    "layer5PushFactor": 0.88,
    "layer6PushFactor": 0.94,
    "maxIterations": 14
  }
}
```

## 🚫 Non-negotiable content rules

Use these when deciding whether content belongs in the map:

- Prefer conceptual anchors over chapter-title scaffolding.
- Layer 2 should usually hold branch-level ideas, not chapter transcripts.
- Layer 3 should usually hold mechanisms, tactics, or consequences.
- Layer 4 is allowed when it materially improves understanding.
- Layers 5 and 6 are exception depths, not defaults.
- If deleting a node barely changes the branch's explanatory power, it
  probably belongs in `detailed-notes.md`, not the map.
- If a branch still feels busy after one consolidation pass, consolidate again.
- Most branches should compress toward:
  - mechanism
  - main consequence
  - operational tactic

## 🛠️ Recommended implementation

- Use **vis-network** as the default rendering library.
- Use a **preset radial layout**:
  - root at the center
  - Layer 1 on a ring around the root
  - deeper layers inside angular sectors owned by their Layer 1 branch
- Set node positions explicitly and mark nodes as fixed. Do **not** rely on a
  physics simulation to discover the radial structure.
- Use ordinary vis-network edges for tree edges.
- Use separate, visually stronger vis-network edges for the black directionality
  spine.
- Use native **vis-network** edges for deeper layers as well unless there is a
  very important reason not to.
- For **Layer 1 review and early iteration**, prefer ordinary **vis-network**
  directional edges first.
- Do **not** hand-draw Layer 1 arrows or edge geometry unless there is a
  demonstrated vis-network limitation that blocks a required layout outcome.
- Do **not** replace ordinary deeper-layer vis-network edges with custom edge
  drawing unless there is a very important reason and the benefit is clear.
- The burden of proof is on custom drawing:
  - show what vis-network could not do
  - show why simpler vis-network edge options were insufficient
  - only then introduce custom geometry
- Use vis-network interactions for zoom, pan, and hover/click detection.
- Include a small fixed legend on the canvas showing the layer names and their colours.
  Keep it visually quiet and out of the main reading path, for example in a bottom corner.
- If the map includes fixed informational UI such as a **legend, inspector, title card,
  or instructions**, provide a simple built-in way to **hide/show those panels** without
  affecting the graph itself.
- The toggle should be:
  - always discoverable
  - usable while zooming and panning
  - suitable for taking uncluttered screenshots or inspecting dense branches
- Prefer **local controls** over one global panel-toggle when possible:
  - the legend should usually have its own small collapse/expand control
  - the inspector should usually be hidden until a node is selected
  - avoid persistent top-level chrome if the control can live on the panel itself
- A small fixed button is still acceptable when there is no better local home for the control.

### Renderer source-of-truth discipline

- Do **not** let the renderer and the layout/content data drift into separate truths.
- If the page supports direct `file://` opening via embedded fallback data, that fallback
  must stay synchronized with the external JSON files that drive normal rendering.
- A layout tweak is **not real** until the actual render path being used by the browser
  has consumed it. Parsing JSON successfully is not enough.
- Configuration key drift is a real failure mode:
  - if `mindmap-layout.json` uses one set of field names
  - but `mindmap.html` reads different field names
  - then the apparent layout fix may be a no-op even though both files look reasonable
- After changing layout knobs, verify that:
  - the renderer is reading the intended keys
  - the visible render actually changes in the expected way
  - the direct-open fallback, if present, is not silently serving stale data
- Prefer a single source of truth or a generated inline snapshot over hand-maintained
  duplicated config blocks.

### 🔓 Bypassing CORS for local file access

- Browsers block `fetch()` on `file://` links for security.
- To ensure the MindMap is portable and viewable by simply double-clicking `mindmap.html`, the renderer **must** include an inline fallback for `mindmap-content.json` and `mindmap-layout.json`.
- The `init()` pattern should be:
  1. Try `fetch()` for external JSON (permits live editing if served via localhost).
  2. If `fetch()` fails or the response is not `.ok`, catch the error and fall back to inlined constants.
  3. Ensure the AI agent updates these inlined constants every time the external JSON files are modified.

## 📐 Layout architecture

Do **not** assume a rigid, concentric radial tree where every node at depth `N`
is the same distance from the center. That often wastes space and creates
visual clutter.

### Preferred mental model

- Treat the map as a **tree + selective graph directionality**.
- **Layer 1** should often behave like a directional storyline or causal chain.
- Lower layers should remain tree-like unless there is a strong reason to add
  directionality.

### Root and Layer 1

- Put the root in the center.
- Keep **Layer 1 small**. As a rule of thumb, aim for about **4–6 Layer 1 nodes**,
  and prefer **5** when the material is large enough to need grouping.
- Lay out the **Layer 1** nodes on a **circular or oval ring** around the root.
- If Layer 1 has an important flow, draw **direct graph edges with arrowheads**
  between the Layer 1 nodes in sequence.
- Prefer native **vis-network** directional edges for that Layer 1 flow before
  attempting any custom-canvas or SVG path work.
- The Layer 1 arrows should connect **node boundary to node boundary**, not float
  disconnected on an inner ring.
- If native vis-network edges already achieve clean boundary attachment and
  readable arrowheads, keep them. Do not replace a working native edge with a
  more complex custom edge just to make the routing feel more bespoke.
- Apply the same bias in deeper layers: if native vis-network edges already give
  clean parent-child ownership and readable routing, keep them.
- If a book has many chapters and no explicit parts/sections, **do not** put every
  chapter at Layer 1. Insert a small number of **grouping/branch nodes** at Layer 1,
  then place the chapters at Layer 2 inside those branch sectors.
- Example:
  - `A Mind for Numbers -> How We Learn -> Chunking -> Procrastination -> ...`

### When to insert grouping nodes

- If putting every chapter on the Layer 1 ring would create a crowded necklace of
  small nodes, that is a sign the hierarchy is wrong, not merely that the spacing
  needs tuning.
- In that case, create **synthetic grouping nodes** that summarize the chapter
  clusters. These can be thematic phases, parts, or other meaningful branch labels.
- The grouping nodes must still be real anchors:
  - they need a clear `what`
  - they need a concrete `why`
  - they should help the reader understand the book's top-level progression
- The directional black spine should run across these grouping nodes, **not** across
  a long ring of chapter nodes.
- **Hard Consolidation Rule**: If a branch tracks a book with many chapters, **prune Chapter-specific nodes** once conceptual anchors are identified. Move the Chapter reference to the node's "Why/Context" metadata and promote the conceptual anchor to the primary node position. This transforms the map from a TOC-mirror to a synthesis-engine.
- The chapters then become Layer 2/3 background context rather than primary nodes.

### Layers 2+

- Do **not** force all nodes at the same layer to be equidistant from the center.
- Use **variable radius** within the same layer:
  - sparse nodes can come inward
  - crowded nodes can move outward
- Nodes at layer `N+1` should generally sit **as close as possible** to their
  parent layer `N`, and only be pushed farther away when needed to avoid overlap.
- Do **not** introduce a large default radial jump just because a deeper layer now
  exists. If a child layer reads as disconnected from its parent, pull it inward
  before enlarging the outer ring.
- The `Layer N -> Layer N+1` gap should stay visually tight enough that the
  child still reads as belonging to the parent branch. If that gap feels too large,
  reduce the next layer radius before changing sector width or node size.
- Prefer **parent-relative gap bands** over absolute global radii.
- Local branch-specific inward adjustments are allowed and often desirable. If one
  branch feels too airy while the rest of the map is fine, tighten that branch
  locally instead of compressing the entire depth band.
- Important: if Layer 1 is drawn as a black directional oval/spine, that spine creates a
  real routing obstacle. Do **not** automatically place Layer 2 closer to the center than
  Layer 1 if doing so forces `Layer 1 -> Layer 2` edges to cut back through the spine's
  interior and cross black, green, or orange routes.
- In books with a strong Layer 1 storyline ring, it can be cleaner to place Layer 2
  **outside** the Layer 1 directional oval, with deeper descendants branching outward
  from there. The correct side of the Layer 1 ring is whichever side preserves the
  clearest routing.
- In other words, "deeper" does **not** always mean "more central." The routing geometry
  takes priority over a rigid inside-out mental model.
- Layers `5` and `6` are allowed, but they are **exception depths**, not normal
  defaults. Use them only when:
  - the chain of explanation is still structurally important
  - collapsing the content upward would blur an important mechanism
  - moving the content to notes would materially weaken the map
- If a branch is the only place that descends to Layer `5` or `6`, keep that depth
  **branch-local**. Do not let one deep branch force the whole map outward.
- As depth increases, the burden of proof increases. In most cases:
  - Layer 4 should be enough
  - Layer 5 should be rare
  - Layer 6 should be very rare
  - anything deeper should almost always move to notes instead

### Sector-based placement

- Give each Layer 1 section its own **angular sector**.
- Place descendants inside that sector.
- Size sectors using both:
  - subtree size
  - node label width
- This prevents wide labels like chapter titles from being squeezed together.
- Within a branch, do **not** reuse one tiny fixed child spread for every sibling group.
  The child fanout must widen based on:
  - number of siblings
  - label width
  - whether deeper descendants are present under those siblings
- If siblings in the same branch begin to stack on nearly the same angle, first:
  - widen the branch-local angular spread
  - then add small **local radial staggering**
  - only after that consider pushing the whole branch farther outward
- **Parallel Bowing Mandate**: Within a single parent's fan of children, do **not** mix different bow directions (e.g. `curvedCW` and `curvedCCW`). Symmetrical bows that converge toward the parent's central ray will intersect one another in the middle of the sector. Instead, force all siblings in a fan to use a single, uniform bow direction. This ensures the edges form concentric, parallel arcs that are mathematically guaranteed never to cross.
- **Tiered Angular Staggering**: When nodes are split into multiple radial tiers within a branch, ensure they are also **angularly offset**. A simple vertical stack (same angle, different radii) creates straight radial edge paths that are prone to cutting through intermediate nodes. An angular drift (e.g. 0.18 radians per tier) ensures a curved clearance path for all edges.
- **Massive Radial Tiering**: If edges are still clipping inner nodes despite angular staggering, increase the physical distance between tiers significantly (e.g., from 100px to 200px). This provides the necessary vertical clearance for curved edges to pass behind inner nodes without overlap.
- **Flattened Curvature**: Edges with high roundness can drift laterally outside their assigned sibling fan and sit on top of unrelated cousin nodes. Reduce edge roundness (e.g., to 0.12 or 0.18) for deeper layers so that arcs remain tightly within their dedicated angular corridors.

### Sector-fraction coupling bug (common pitfall)

**Problem**: If you size L1 sectors by total subtree depth (including L3+) and then
derive L2 angular spread as a fixed fraction of the L1 sector
(e.g. `halfSpan = parent._sectorSpan * 0.45`), adding deep L3 subtrees
inflates the L1 sector — which then spreads the few L2 nodes over a much
wider angle than they need. The result: some L2 nodes appear far from their
L1 parent even though the radial gap is the same.

**Prevention**: **Decouple L2 spread from L1 sector size.** Compute each
layer's angular spread from that layer's own node count and label widths —
not as a fraction of its parent's sector. A concrete fix:

```js
// BAD: ties L2 spread to the inflated L1 sector
const halfSpan = parent._sectorSpan * 0.45;

// GOOD: size L2 spread by number of children, capped by sector
const perNodeAngle = 0.22; // radians — tune for typical label width at R2
const halfSpan = Math.min(parent._sectorSpan * 0.45, nk * perNodeAngle / 2);
```

The L1 sector can remain subtree-proportional for spacing purposes; only the
**placement spread within** that sector needs to be independently sized.

### Sub-sector confinement for deeper layers

When placing Layer N+1 nodes, confine them to a **sub-sector** derived from
the gap between their L(N) parent and its nearest sibling — not from a fixed
angular constant. If you use a fixed constant, adjacent siblings' children
will spill into each other's angular territory, and their edges will cross
after collision resolution pushes the nodes apart.

```js
// For each L2 node placing its L3 children:
const prevA = ki > 0 ? kids[ki-1]._angle : kid._angle - siblingGap;
const nextA = ki < nk-1 ? kids[ki+1]._angle : kid._angle + siblingGap;
const maxHalf = Math.min(|kid._angle - prevA|, |nextA - kid._angle|) * 0.42;
const halfSpan3 = Math.min(desiredSpread, maxHalf); // never exceed available sector
```

Note: collision resolution fixes **node overlap** but creates **crossing
edges** when it pushes nodes from different parents toward each other. The
sub-sector constraint prevents this at the source.

- For small groups of deeper children, such as `2` anchors under one chapter,
  place them inside a **parent-local sub-sector** derived from the neighboring
  sibling gaps, and allow a slight **inner/outer radius stagger** when needed.
- Do **not** stack detailed anchors from adjacent parents at nearly the same
  angle and radius. That creates unreadable bundles even if the math says the
  nodes barely do not touch.
- Important: a child fan can be locally valid within its parent sub-sector and still
  collide with **cousin nodes** from the adjacent parent. At deeper layers, add:
  - extra **outward staggering** when neighboring parent angles are tight
  - and, if needed, a same-depth **global collision pass** across all nodes in that
    deeper layer
- In other words, validate not just parent↔child placement, but also
  **cousin↔cousin spacing** at the same depth.
- Another common failure mode: the node placement is locally fine, but the **lane
  assignment for routed child edges is wrong**. If second-row or outer-tier children
  repeatedly route through first-row siblings, do not keep widening spreads alone.
  Reassign route lanes from the child's actual left/right column or tier position.
- In dense Layer 3 fans, raw child index is not a safe routing proxy. Two children can be
  adjacent in index order while living on opposite sides of the local fan after collision
  resolution or tiering. Use the actual placed geometry or explicit column role.
- If a branch's deeper children keep failing as a 2x2 or multi-tier local fan, prefer a
  cleaner one-row fan or another simpler arrangement. Do not preserve a fragile local
  matrix merely because it looks symmetric in code.
- After simplifying a deeper local fan into a clean single row, re-tune the routing
  aggressiveness. High tangent offsets or exaggerated lane bows that were justified in a
  denser multi-tier fan can become needless visual clutter once the route is clear. In that
  case, prefer the shortest clean local edge that still passes geometry validation.
- Also do not assume the generic parent→child tree route should survive unchanged after
  that simplification. A single-row Layer 3 fan often deserves its own lower-bow local
  route shape. If the edge is valid but still looks scenic, theatrical, or over-designed,
  the route model is still too heavy for the simplified geometry.

### Collision handling

- After the first layout pass, do a **collision-resolution pass**.
- Check for overlapping node bounding boxes within the same depth.
- If two nodes overlap, push the later/lower-priority one outward slightly.
- Keep doing this until overlaps are gone or a guard limit is reached.
- **Warning**: collision resolution can introduce crossing edges for nodes
  from different parents. Prevent this with sub-sector confinement (above)
  rather than fixing it after the fact.
- Run collision handling **after final node sizing and emphasis styling** are
  known. A layout that only works before stroke/font scaling is not valid.
- Node collision handling is **not sufficient**. After node overlap is solved,
  run a separate pass for:
  - edge ↔ node intersections
  - edge ↔ edge intersections
- If a node move fixes one overlap but creates a routing conflict, keep
  iterating. The finished map must satisfy all three conditions:
  - node ↔ node non-overlap
  - edge ↔ node non-intersection
  - edge ↔ edge non-intersection where avoidable
- When a whole sibling fan overlaps, treat that as a **placement parameter**
  failure, not just a collision-pass failure. Recompute that branch's spread
  and local radii instead of repeatedly nudging individual nodes.
- For deeper layers, if several nearby parents each have their own valid local fans,
  but those fans overlap each other, treat that as a **regional cousin-collision**
  problem. Fix it by increasing outward radius or running a deeper-layer collision
  pass before resorting to arbitrary label shrinkage.
- Do not validate dense regions one layer at a time. If Layer 3 and Layer 4 occupy
  the same branch sector, run collision handling across **both layers' placed
  footprints**, because a locally valid red fan can still collide with nearby orange
  nodes.
- For crowded deeper children, use **multi-tier placement by default** instead of a
  single compressed fan. Splitting `4+` grandchildren into inner/outer tiers is more
  stable than relying on late outward nudges.
- Center-to-center distance is too weak for collision checks on wrapped ellipse
  nodes. Use an **estimated node footprint** based on width constraint, line count,
  and final styling when deciding whether two placed nodes still overlap.
- If one branch accumulates many Layer 3 and Layer 4 nodes that mostly restate each
  other, do not preserve that granularity. Consolidate them into fewer nodes that
  capture the **mechanism**, the **main consequence**, and the **operational tactic**.
- A good test: if removing one node barely changes the branch's explanatory power,
  that node is probably branch clutter rather than a real anchor.
- Once a branch has been consolidated into stable conceptual anchors, move the
  chapter-specific leftovers out of the map and into a separate **chapter-organized
  notes file**. The map should preserve structure; the notes should preserve residue.
- If a branch still feels busy after one consolidation pass, consolidate **again**.
  Do not assume one round is enough. Keep collapsing until the branch reads as a
  handful of durable ideas rather than a compressed outline.
- Treat **same-depth node overlap** as a hard failure, not a cosmetic issue. This is
  especially important for Layer 3 and Layer 4 local fans, where routing work can
  improve edges while quietly causing orange-on-orange or red-on-red node collisions.
- Stronger rule: **technical non-overlap is not enough** in dense deeper layers.
  Layer 3 and Layer 4 nodes need **visible breathing room** between ellipses, not
  just mathematically non-intersecting footprints.
- A branch can still fail even if the ellipses do not literally intersect, when the
  visible gap is so small that the nodes read as touching or merged.
- A routing fix that introduces node overlap is still invalid. The finished branch must
  satisfy all of these at once:
  - node ↔ node non-overlap
  - node ↔ node comfortable visible separation
  - edge ↔ node non-intersection
  - edge ↔ edge non-intersection where avoidable
- For crowded Layer 3 fans, prefer **one node per tier** before accepting a cramped
  multi-node row with weak breathing room.
- Dense local fans must be checked both:
  - within the same parent's children
  - across neighboring parents' children at the same depth
  because cousin overlaps are easy to miss when focusing only on one chapter fan at a time.

### Edges

- Tree edges should be simple and readable.
- Use **radial elbow links** for parent→child tree edges, not straight lines
  or generic outward beziers. The control points must be computed as follows:
  - `cp1` = (cos(parent_angle) × rMid, sin(parent_angle) × rMid)
  - `cp2` = (cos(child_angle) × rMid, sin(child_angle) × rMid)
  - where `rMid = (rParent + rChild) / 2`
  - Draw as a cubic bezier: `M ps C cp1 cp2 ce`
  - This guarantees the edge exits the parent radially outward, arcs at the
    midpoint radius, and enters the child radially — **never crossing any node
    at an intermediate radius**.
- For **peer flow arrows** (L1→L1 sequential), bow outward past the ring:
  - Prefer the **shortest local outward arc** between neighboring L1 nodes.
    Do **not** send the arrow around a global perimeter unless the local arc
    fails validation.
  - Start from the direct chord between the two node boundaries, then add a
    modest outward normal offset to create a quadratic bezier. This keeps the
    arrow visually local instead of producing huge scenic loops.
  - Penalize total route length when comparing candidate L1 arrows. If two
    routes are equally valid, choose the shorter, tighter one.
  - If a peer flow arrow still looks cramped or awkward, fix the **node spacing**
    before inventing a more complex route. In particular, slightly separate the
    two neighboring Layer 1 nodes so a normal local arc has room to read cleanly.
  - Handle angle wrap-around: `dA = aB - aA; if (dA > π) dA -= 2π`.
  - **Important**: it is not enough for the arrow to stay outside the L1 ring.
    It must also stay outside the **descendant envelope** of the two adjacent
    L1 sections. In practice, compute the outer radius using the maximum
    subtree extent of those sections, then add margin. Otherwise the black
    storyline arrow will visibly cut through green/orange child edges.
  - Also attach the arrow to the **outward radial side** of each L1 node, not
    merely to the boundary point in the control-point direction. Otherwise the
    arrow can still enter a section through its local child fanout.
- Treat the entire Layer 1 directional oval as reserved routing territory. If child edges
  repeatedly cross that oval, the fix is often to move the child layer to the **outside**
  of the oval rather than to keep inventing tighter bends through the interior.
- Compute edge endpoints on the **node ellipse boundary** toward the other
  node — not at the node center. Use the parametric ellipse formula:
  `t = 1 / sqrt((ux/rx)² + (uy/ry)²)` to find the boundary point along
  direction (ux, uy).
- For arrowheads on bezier paths, shorten the endpoint slightly along the
  bezier tangent (control→endpoint direction) so the arrowhead sits at the
  node boundary, not overlapping it.
- If an edge connects two nodes of different layers, the edge color should be
  the color of the **deeper-layer node**.
- Avoid routing edges through the center if that creates crossing or clutter.
- Do **not** let edges cross if a cleaner layout is possible.
- Treat every non-endpoint node ellipse as an **obstacle**. A routed edge must
  stay outside that obstacle with visible clearance, not merely avoid the
  ellipse center.
- Treat existing routed edges as obstacles as well, especially for peer-flow
  arrows. A visually ambiguous near-overlap is a layout failure even if the
  SVG paths do not mathematically cross.
- When routing an edge, check the full curve or a sufficiently dense set of
  sampled points against:
  - every non-endpoint node ellipse, expanded by a padding margin
  - every already-accepted edge path, also expanded by a padding margin
- If a route fails either check, do **not** keep it. Reposition local nodes,
  widen the sub-sector, push one branch outward, or choose a different outward
  bow/control radius and test again.
- When the remaining failures localize to a branch boundary, do not assume the dirty
  branch is the only thing that should move. It is often cleaner to rotate or widen the
  neighboring branch's first child fan deeper into its own sector so the boundary becomes
  explicit instead of contested.

### Routing validation

Before considering the map complete, run a final validation pass on the
**actual rendered geometry**:

- Use final ellipse radii, stroke widths, font sizes, and arrowhead offsets.
- Validate that no edge intersects or visually runs through any non-endpoint
  node.
- Validate that no two edges intersect or visually merge into one another in a
  confusing way.
- Validate this after any collision-resolution adjustments, because a valid
  pre-adjustment route can become invalid after nodes move.
- Validate in a **real browser render**, not only by geometric reasoning.
  Anti-aliasing, stroke coverage, and browser SVG rendering can reveal visual
  seams or near-merges that are not obvious from pure math.
- In practice, render the mind map in **headless Google Chrome** and inspect the
  screenshot against the checklist below. Do not rely only on code inspection or
  mathematical layout reasoning when deciding whether the map is acceptable.

Important: screenshot inspection alone is **not** a sufficient authority for
edge-crossing validation in dense regions. A screenshot reviewer can miss real
crossings when several thin curves run near each other.

Treat the final routing gate as a **two-part requirement**:

1. a geometry-aware validation step by the renderer or the main agent
   - check same-depth node footprints against each other
   - sample or otherwise check routed edges against non-endpoint nodes
   - sample or otherwise check routed edges against other routed edges
   - fail the layout if a node overlap, crossing, or obstacle violation is detected
2. a browser screenshot review
   - used to catch visual ambiguity, anti-aliasing artifacts, and hierarchy failures
   - not used as the sole proof that routing is correct

If the screenshot looks acceptable but the geometry-aware pass fails, the map is
still invalid. If the geometry-aware pass succeeds but the screenshot reveals a
confusing visual merge, the map is also still invalid.

Also treat renderer startup failure as a blocking validation failure. If the graph does
not render, the validation panel remains in a placeholder state, or the browser shows
only the background chrome without nodes and edges, the map is not "partially valid" —
it is simply broken and must be fixed before any QA review.

Every time you inspect the mind map in a browser, consult this checklist:

1. No edges should cross other edges or nodes.
2. Layer 1 must preserve directionality, with all black flow edges showing arrowheads.
3. Every edge must visibly terminate inside or at its target node. No edge may end
   short or appear left dangling.

Do **not** treat "mostly readable" as acceptable if this checklist fails in a dense
branch. A branch can feel usable at a glance and still be invalid because orange,
green, or black edges cross or merge when inspected closely.

When reviewing a dense region, inspect it in at least two ways:

- the full-map screenshot, to judge hierarchy and overall balance
- a zoomed-in branch inspection, to judge actual routing between nearby nodes

If a crossing or confusing edge merge is visible only in the zoomed-in view, it is
still a layout failure and must be fixed before the map is considered complete.

If validation fails, the layout is not acceptable yet.

### Directionality and causal flow (The "Single Arrow OR Edges" Rule)

- **The Universal Rule**: AT ANY LAYER, a node can have either a **single directional arrow out** (denoting a sequence or process step) OR **multiple plain edges out** (denoting a category/hierarchy). A node must **never** originate both.
- **Arrows = Directionality**: Arrows denote a sequence or causal chain. While this is primarily the main spine (`Root → L1a → L1b → ...`), directionality can absolutely exist at deeper layers (2, 3, 4, etc.) to represent a sub-process. Directional edges should be distinct (e.g., solid black `#222`) with clean arrowheads.
- **Plain lines = Hierarchy**: Parent-child connections denoting category or detail MUST be plain edges with **NO arrowheads**.
- The **root node** must only have a single directional arrow out to the first Layer 1 node, establishing the entry point. It must have **no ordinary tree edges** to Layer 1.
- **Do not mix representations**: Once a directed arrow exists between two nodes, any plain edge on the same path is redundant and creates visual noise.

## 🔤 Text & oval sizing

Nodes should render as **white ellipses** in vis-network, with centered text.
Size nodes from wrapped label text rather than using one global fixed node size.

Practical sizing guidance:

```js
const PAD_X = 11;
const PAD_Y = 7;
const LINE_H = 13;
const width = Math.maxLineLength * fontSize * 0.62 + PAD_X * 2;
const height = lineCount * LINE_H + PAD_Y * 2;
```

- Allow **up to 3 lines** for chapter nodes so ellipses stay narrow enough to fit.
- Increase width for wider labels before increasing radius of the whole ring.
- Chapter node names can use ` · ` as a separator:
  - `"Ch 2 · Focused vs Diffuse Modes"` -> `["Ch 2", "Focused vs", "Diffuse Modes"]`

## 🎨 Layer colours

Use white fill by default. Emphasize importance through **stroke, font weight,
font size, and edge weight/opacity**, not through colored fills.

| Layer | Colour             | Hex (Vivid) |
|------:|--------------------|-------------|
| 0     | Near-black         | `#222`       |
| 1     | Dark grey          | `#444`       |
| 2     | Vivid Green        | `#00c853`    |
| 3     | Electric Orange    | `#ff9100`    |
| 4     | Vivid Crimson (Red)| `#ff1744`    |
| 5     | Sky Blue           | `#3498db`    |
| 6     | Deep Purple        | `#8e44ad`    |

- **Color Uniformity Mandate**: For every node, the **Font Color** must precisely match the **Border Color**. Use font-weights of 600+ to ensure legibility of these vibrant hues against white backgrounds.

- The rendered map should include a compact legend that maps these layer colours
  to layer names. This helps the viewer decode the map quickly without guessing.
- The legend labels must match the **current map semantics**, not stale assumptions
  from an earlier version. If a layer now contains grouping nodes or mixed anchor
  types, use broader labels like `Branch anchors` or `Detailed anchors` instead
  of outdated labels like `Chapters`.
- If deeper layers are actually present in the current map, name them explicitly in
  the legend as well, for example `Deeper anchors`, instead of leaving them as bare
  `Layer 4`, `Layer 5`, and so on.
- Because legends and inspectors are overlays, they must be easy to temporarily hide;
  otherwise they can obstruct branches during review and screenshot validation.
- Panel placement must avoid panel-on-panel collisions:
  - keep the **Manifest** in the top-left by default
  - keep the **Legend** in the bottom-right by default
  - if a scope hint or other fixed chip exists in the same corner, keep vertical
    clearance so the legend does not overlap it
- Inspectors should usually behave like **selection drawers**, not permanent dashboards:
  - hidden by default
  - open when a node is clicked
  - close when the same node is clicked again or the canvas is cleared
  - switch content when another node is selected

## 🌟 Emphasis and importance

Do **not** emphasize everything at a layer equally.

### Rules

- Emphasis should be **selective**.
- A node should only be strongly emphasized if its importance is **clearly
  higher than its peers**.
- Most nodes should remain visually quiet.
- Do **not** emphasize nodes merely because they are:
  - at a particular layer
  - the first child in a branch
  - parents of other nodes
  - recently added
- Use emphasis to surface:
  - the root idea
  - a small number of core mechanisms
  - a few truly central chapter anchors

### Visual distinction mandate (The "Core Path" Rule)

- Emphasized items must **drastically** contrast with non-emphasized items, establishing a clear "Core Reading Path".
- Do not let the map devolve into a homogenous web of equal-weight ovals and lines.
- **Opacity Fading**: Non-emphasized nodes and edges must visually stretch into the background. Use severe opacity fading (`#hex88` down to `#hex55`) for the borders, text colors, and edges of standard detail nodes.
- **Drastic Scaling Differentials**: Emphasized connections should be dramatically heavier. 
  - Scale up fonts significantly (e.g., jumping from 13px to 18px).
  - Use thick, fully opaque bounding strokes.
  - Use thick, fully opaque edges (e.g., 3.5px to 4.5px) compared to thin (1.0px) standard hierarchical paths.

### Avoid

- emphasizing every Layer 2 chapter
- emphasizing all nodes with children by default
- using fill color to imply importance
- leaving baseline nodes and edges too dark or fully opaque, which flattens the hierarchy into visual noise
- using repetitive edge labels like `"begin"` / `"then"` unless they genuinely help

### Practical recommendation

- Use **3 tiers at most**:
  - strong
  - medium
  - baseline
- Strong tier should be **small**.
- As a rule of thumb, keep emphasized nodes to a **small minority** of the map.
  If most nodes at a given layer feel equally loud, the hierarchy has failed.
- Baseline nodes should be visibly quieter than emphasized nodes:
  - lighter stroke
  - lighter text colour or opacity
  - thinner / lighter tree edges
  - weaker shadow
- If emphasis is not reading clearly, first **de-emphasize the baseline** before making strong nodes louder.
- Border width should increase only modestly. Prefer contrast from text weight, node size,
  shadow, and edge treatment before resorting to heavy outlines.
- It is usually better to maintain an explicit **importance allowlist** of the few nodes
  that deserve emphasis than to infer importance from broad heuristics like depth or
  child count.

## 📦 Data shape

```js
const tree = {
  name: "Root label",
  layer: 0,          // 0–6, controls colour
  what: "What is it? Explanation shown on click.",
  why: "Why is it important? Explanation shown on click.",
  children: [ /* same shape, recursively */ ]
};
```

Optional implementation detail:

- Keep a separate `importanceScore(node)` function in the renderer rather than
  storing importance directly in the data unless there is a good reason.

## 🧭 MindMap content conventions

- **Always include the full Layer 1 skeleton first**:
  - root -> parts/sections -> all chapters in the book
- If the source has **too many top-level items** for a readable Layer 1, create
  intermediate grouping nodes so Layer 1 stays near **5** nodes and the chapters
  move to Layer 2.
- **Unread chapters still appear as nodes** at their current highest completed
  layer.
- **Every node should represent an anchor, not a detailed note**.
- **Every retained node should clear an importance bar**.
- **Descend only when actually read at that layer**.

### Cross-chapter consolidation

- After you have descended far enough into a cluster of adjacent chapters, **do not**
  keep the map as a permanent chapter-by-chapter excavation log.
- If several chapter-specific nodes are now expressing the same underlying ideas,
  replace them with a smaller set of **synthesized conceptual anchors**.
- This consolidation can happen at layers 2–4:
  - remove chapter-specific nodes that have become scaffolding
  - create better cross-chapter nodes that capture the durable learning
  - preserve the depth where it is valuable, but rename the nodes around the ideas,
    not around the chapter titles
- A good test is:
  - if the node matters mainly because of **where it came from**, it is probably scaffolding
  - if the node matters because it expresses a **reusable idea**, it is probably worth keeping
- The map should increasingly reflect your understanding of the material, not your
  reading itinerary.

### Tooltip contract

- `name` = concise anchor
- `what` = "What is it?" explanation in plain prose, usually `1–5` sentences
- `why` = "Why is it important?" explanation in plain prose, usually `1–3` sentences
- `children` = sub-anchors only, not supporting trivia

### Prioritisation rules

- If you cannot explain **why** a node matters concretely, it is usually too
  weak to keep.
- Prune redundant or low-signal children aggressively.
- Prefer a smaller map of consequential anchors over a larger map of weak ones.
- When several chapter-specific nodes collapse into the same takeaway, keep the
  synthesized takeaway and prune the duplicate chapter-specific framing.

### Branching rules

- Keep branching cognitively manageable.
- A node should have **at most 5 direct children**.
- If a node would exceed `5` children, insert an intermediate grouping node.
- This is a hard content-structuring rule, not a loose guideline.
- For whole-book maps, apply this rule aggressively at the top:
  - root should usually connect to only a small set of branch anchors
  - branch anchors should usually own the chapter nodes
  - chapter nodes should own deeper reading anchors

## 🔭 Zoom & pan

Use a single zoom instance:

```js
const zoom = d3.zoom().scaleExtent([0.1, 4])
  .on('zoom', e => g.attr('transform', e.transform));
svg.call(zoom);
zoom.transform(svg, d3.zoomIdentity.translate(W / 2, H / 2).scale(0.2));
```

- Tune initial scale to fit the actual map.
- If outer layers move far outward because of collision resolution, lower the
  initial zoom.
- Do **not** hard-cap the initial zoom to a tiny value if the map bounds would
  support a larger readable scale. The fit should be driven by actual rendered
  bounds, otherwise the map can appear absurdly small even when the layout is
  valid.

## ⚠️ Common pitfalls

- **Two zoom instances** break centering.
- **Edges not actually touching nodes** makes directionality look fake.
- **All nodes at a given layer having the same radius** wastes space and creates
  the false impression of rigid rings.
- **Putting every chapter at Layer 1 in a long book** usually produces a dense,
  low-signal outer ring. The fix is to add grouping nodes, not merely to shrink
  labels or enlarge the canvas.
- **Keeping chapter-specific scaffolding after the ideas have already been synthesized**
  turns the map into a reading transcript instead of a high-signal conceptual model.
- **Layer `N+1` too far from layer `N`** makes the tree feel disconnected.
- **Over-emphasis by layer** makes everything look equally important.
- **Auto-emphasizing the first child, every parent, or every node in a favored layer**
  quickly destroys the visual hierarchy. Importance must be assigned sparingly and
  deliberately.
- **Wide chapter labels not accounted for in sector sizing** causes overlaps.
- **Using the same narrow angular spread for every sibling group** causes
  stacked nodes and bundled edges, especially when several children have
  similarly long labels or deeper descendants.
- **Checking only sibling overlap but not cousin overlap** misses a common
  failure mode in deep maps: each local fan looks valid, but neighboring fans
  collide in the same region of the canvas.
- **Computing link boundaries before final node size is known** produces bad edge
  endpoints.
- **Collision handling only before styling** can fail once emphasized nodes grow.
- **Fixing node overlap without rechecking routes** allows edges to cut through
  nodes or through neighboring branches.
- **Assuming bezier control points are safe without validation** leads to edges
  that mathematically route into ovals or visually merge with other edges.
- **Treating a routing-model bug like a spacing bug** wastes time. If the same
  edge-node conflict repeats across several sibling pairs after multiple spread/radius
  tweaks, stop parameter tuning and change the lane logic or route shape itself.
- **Leaving old high-bow routing in place after simplifying the fan** produces edges that
  technically validate but still look needlessly scenic. Once the node geometry is clean,
  reduce routing aggression to match the simpler structure.
- **Reusing the generic tree-edge curve for a simplified single-row Layer 3 fan** can
  produce edges that still look wrong even after validation passes. Use a lighter local
  route shape for that case instead of assuming one curve model fits every density.
- **Treating edge crossings as acceptable cleanup debt** degrades readability
  fast. Resolve them in layout/routing, not in prose.
- **Routing L1 storyline arrows only outside the L1 ring** is insufficient;
  they must clear the outer extent of nearby subtrees as well.
- **Capping fit-to-bounds zoom too low** can make the whole map tiny and hide
  problems during review.
- **Edge labels added by default** often clutter the map. Only use them when they
  add real meaning.
- **Fixed UI panels with no hide/show control** make it harder to inspect dense regions
  and can hide layout problems near the edges of the canvas.
- **Persistent inspectors that stay open even when nothing is selected** waste canvas
  attention and create low-value clutter.
- **Global hide/show buttons for small local panels** are often heavier than necessary
  when the panel itself can host its own collapse control.

## Postmortem Checklist

After each major layout/routing pass, pause and classify the remaining defects before tuning more numbers:

- Are the remaining failures primarily node overlap, edge-node intersection, edge-edge intersection, or branch-boundary conflicts?
- Do several failures share the same row/tier/lane pattern? If so, change the generating rule instead of widening the whole map again.
- Is the dirty region local to one branch boundary? If so, test rotating or widening the neighboring branch sector, not just the branch that owns the failing edge.
- Has the fan shape become more complex than necessary? If a simpler one-row or otherwise clearer local arrangement would remove the repeated failure mode, prefer the simpler arrangement.
- Do not call the map done until the browser-rendered validation panel itself reports a pass.
