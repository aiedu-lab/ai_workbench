# Concept & Exercise: Embeddings Visualization

## 🎯 Objective

See word embeddings as geometry — run GloVe on a small word
list and observe how meaning becomes position, direction, and
distance in a 50-dimensional vector space.

---

## 🧠 The Core Concept

Every word maps to a vector of numbers. Words with similar
meaning cluster nearby; meaning is geometry. The classic
demonstration:

> **king − man + woman ≈ queen**

This works because gender is a direction in the vector space,
not a label. Cosine similarity measures the angle between two
vectors — high similarity (≈ 1) means nearly parallel; low
(≈ 0) means orthogonal; negative means opposite.

Embeddings underpin every modern AI system: the LLM reads
tokens as vectors, the attention mechanism shifts each
vector based on its neighbors (context), and the output is
decoded back to words. This exercise makes those mechanics
visible.

> **Reference:** Grant Sanderson (3Blue1Brown) — [Attention
> in transformers, visually explained](
> https://www.3blue1brown.com/?topic=neural-networks&lesson=gpt)

---

## 🛠️ Setup

Complete the [Embedding Setup](
dev_workbench.md#embedding) in the Development Workbench
session, then run:

```bash
cd projects/embedding
source .venv/bin/activate
python3 embed.py
```

In VS Code, run cells individually — the 2 × 3 figure renders
inline in the output panel. Running as a plain script saves
`embedding_map.png` in the same directory.

> **VS Code cell-by-cell:** open `projects/embedding/embed.py`
> in VS Code. It is annotated with `# %%` markers (jupytext
> format). VS Code detects these and shows **Run Cell**
> buttons above each cell — run Cell 0 to load GloVe, then
> Cell 1 to render the figure.

---

## Exercises

Run `embed.py` once to generate all six panels, then work
through the exercises panel by panel.

### Exercise 1 — Embedding Map (5 min)

**Panel (0,0):** PCA projects 11 words from 50 dimensions
to 2 dimensions for our screen.

Discussion questions:
- Which words land closest together? Furthest apart?
- `apple` and `bicycle` sit far from the architectural
  cluster. Why?
- What does "distance" represent here?

---

### Exercise 2 — Clustering (5 min)

**Panel (0,1):** The same PCA projection with cluster
regions annotated (structural, vertical, unrelated).

Discussion questions:
- The structural group (building, skyscraper, dome, …) forms
  a tight neighborhood. What do those words share in
  training data?
- `tower` and `lighthouse` cluster separately — what
  dimension separates them from the broader structural group?

---

### Exercise 3 — Concept Direction (10 min)

**Panel (0,2):** PCA of king / man / woman / queen with
arrows showing king→queen and man→woman.

**Panel (1,2):** Top-5 words from
`king − man + woman` in 50-D space.

Discussion questions:
- Are the two arrows roughly parallel? They should be —
  gender is a direction, not a category.
- Does `queen` appear at rank 1 in Panel (1,2)? If not,
  what does appear and why might that be?
- Try substituting other analogy pairs mentally: what
  direction encodes plurality? Tense?

---

### Exercise 4 — Similarity (10 min)

**Panel (1,0):** Horizontal bars for five word pairs.

| Pair | Expected score |
|---|---|
| king / queen | high (≈ 0.75) |
| man / woman | high (≈ 0.85) |
| dog / cat | medium-high |
| tower / skyscraper | medium |
| apple / bicycle | low |

Discussion questions:
- Which pair is most similar? Does that match your
  intuition?
- High dot product → similar *usage context*, not just
  meaning. What does that imply about `man` and `woman`?
- In a RAG system, cosine similarity decides which document
  chunks are injected into the prompt. What happens if the
  threshold is too high? Too low?

---

### Exercise 5 — Nearest Neighbors / Attention (10 min)

**Panel (1,1):** Top-5 neighbors of `neural`, `computer`,
and `king`.

Discussion questions:
- `neural` neighbors: do they reflect AI/ML terminology?
- `king` neighbors: royalty terms, or something surprising?
- In transformers, each token's embedding is *shifted* by
  its neighbors via the attention mechanism — similar to how
  the nearest-neighbor list changes depending on which words
  surround a word in a sentence. This panel shows the static
  GloVe neighborhood; attention makes it dynamic.

---

## 🔗 Connection to RAG

The cosine similarity you just observed is the exact
calculation used in Retrieval Augmented Generation (RAG):
a query embedding is compared against document-chunk
embeddings, and the closest chunks are injected into the
prompt as context. See [§8 Embeddings & RAG](
prompting_advanced.md#8-embeddings--retrieval-augmented-generation-rag)
in the Advanced Prompting session for the full pipeline.
