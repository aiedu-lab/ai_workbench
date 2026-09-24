# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python (.venv)
#     language: python
#     name: .venv
# ---

# %% [markdown]
# # Word Embedding Visualizations
#
# Six panels showing how GloVe 50-dim word vectors behave:
# embedding map, clustering, concept direction, similarity,
# nearest neighbors, and concept direction result.

# %%
import os
import math
import pathlib
import numpy as np
import matplotlib

# Jupyter/VS Code: ipykernel defaults to inline — don't override it.
# Terminal only: WebAgg (open URL manually) or Agg (saves PNG).
def _setup_backend():
  try:
    if get_ipython() is not None:  # type: ignore[name-defined]
      return
  except NameError:
    pass
  try:
    import tornado  # noqa: F401
    matplotlib.use('WebAgg')
    matplotlib.rcParams['webagg.open_in_browser'] = False
  except ImportError:
    matplotlib.use('Agg')

_setup_backend()

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from sklearn.decomposition import PCA
import gzip
import urllib.request

# AI-GENERATED: Phase 50 Step 50.8 (plan.md)
# GloVe is loaded with plain NumPy instead of gensim: gensim's C
# extensions do not build on Python 3.14. WordVectors mirrors the
# few gensim KeyedVectors calls the panels below use.
class WordVectors:
  """Word → vector lookup with gensim-compatible similarity calls."""

  def __init__(self, words, vectors):
    self.words = [str(w) for w in words]  # plain str, not np.str_
    self.index = {w: i for i, w in enumerate(self.words)}
    self.vectors = vectors
    # Unit-length copy so cosine similarity is a plain dot product.
    self.unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

  def __len__(self):
    return len(self.words)

  def __getitem__(self, word):
    return self.vectors[self.index[word]]

  def similarity(self, a, b):
    """Cosine similarity of two words."""
    return float(self.unit[self.index[a]] @ self.unit[self.index[b]])

  def most_similar(self, positive, negative=(), topn=10):
    """Top-n (word, cosine) pairs nearest to sum(+positive −negative).

    Same rule as gensim: average the unit vectors (negatives
    subtracted), then rank all words, skipping the input words.
    """
    if isinstance(positive, str):
      positive = [positive]
    terms = [self.unit[self.index[w]] for w in positive]
    terms += [-self.unit[self.index[w]] for w in negative]
    query = np.mean(terms, axis=0)
    query /= np.linalg.norm(query)
    scores = self.unit @ query
    skip = {self.index[w] for w in (*positive, *negative)}
    ranked = (i for i in np.argsort(-scores) if i not in skip)
    return [
      (self.words[i], float(scores[i]))
      for _, i in zip(range(topn), ranked)
    ]


# Same file gensim.downloader fetches for "glove-wiki-gigaword-50":
# gzip text, a "400000 50" header, then "word v1 … v50" per line.
GLOVE_URL = (
  "https://github.com/RaRe-Technologies/gensim-data/releases/"
  "download/glove-wiki-gigaword-50/glove-wiki-gigaword-50.gz"
)


def _load_glove(cache):
  """Load GloVe from the .npz cache, downloading it on first use."""
  if os.path.exists(cache):
    print("Loading GloVe from cache…")
    data = np.load(cache)
    return WordVectors(data["words"], data["vectors"])
  print("Downloading GloVe (~65 MB)…")
  # Stream line by line into a preallocated array; splitting the
  # whole file at once would hold ~20M small strings in memory.
  with urllib.request.urlopen(GLOVE_URL) as resp, \
      gzip.open(resp, "rt", encoding="utf-8") as lines:
    count, dim = map(int, next(lines).split())
    words = []
    vectors = np.empty((count, dim), dtype=np.float32)
    for i, line in enumerate(lines):
      word, *values = line.rstrip("\n").split(" ")
      words.append(word)
      vectors[i] = np.asarray(values, dtype=np.float32)
  words = np.array(words)
  np.savez(cache, words=words, vectors=vectors)
  return WordVectors(words, vectors)


# __file__ undefined in notebooks; cwd is the script/notebook dir
try:
  _dir = pathlib.Path(__file__).parent
except NameError:
  _dir = pathlib.Path.cwd()
model = _load_glove(str(_dir / "glove_50.npz"))
print(f"Ready: {len(model)} words loaded.")

# %%
# --- Multi-panel figure: 2 rows × 3 cols ---
fig, axs = plt.subplots(2, 3, figsize=(15, 9))

# Helper: PCA-project a list of words to 2-D
def _project(words):
  vecs = np.array([model[w] for w in words])
  return PCA(n_components=2).fit_transform(vecs)

# ─── Panel (0,0): Embedding Map ────────────────────────────
ax = axs[0, 0]
scatter_words = [
  'tower', 'building', 'skyscraper', 'roof', 'built',
  'dome', 'facade', 'constructed', 'lighthouse',
  'apple', 'bicycle',
]
pts = _project(scatter_words)
ax.scatter(pts[:, 0], pts[:, 1], c='steelblue', edgecolors='k')
for i, w in enumerate(scatter_words):
  ax.annotate(
    w, (pts[i, 0], pts[i, 1]),
    xytext=(5, 2), textcoords='offset points',
    fontsize=8,
  )
ax.set_title("(1) Embedding Map")
ax.grid(True, alpha=0.3)

# ─── Panel (0,1): Clustering ───────────────────────────────
ax = axs[0, 1]
groups = {
  'structural': (['building', 'skyscraper', 'roof', 'dome',
                  'facade', 'constructed', 'built'], 'salmon'),
  'vertical':   (['tower', 'lighthouse'],            'gold'),
  'unrelated':  (['apple', 'bicycle'],               'lightgreen'),
}
all_cluster_words = [w for ws, _ in groups.values() for w in ws]
cpts = _project(all_cluster_words)
word_to_pt = dict(zip(all_cluster_words, cpts))
for label, (words, color) in groups.items():
  xs = [word_to_pt[w][0] for w in words]
  ys = [word_to_pt[w][1] for w in words]
  ax.scatter(xs, ys, c=color, edgecolors='k', label=label, s=80)
  for w in words:
    ax.annotate(
      w, word_to_pt[w],
      xytext=(4, 2), textcoords='offset points', fontsize=8,
    )
ax.legend(fontsize=7)
ax.set_title("(2) Clustering")
ax.grid(True, alpha=0.3)

# ─── Panel (0,2): Concept Direction scatter ────────────────
ax = axs[0, 2]
dir_words = ['king', 'man', 'woman', 'queen']
dpts = _project(dir_words)
dmap = dict(zip(dir_words, dpts))
colors = ['royalblue', 'orange', 'orchid', 'crimson']
ax.scatter(
  dpts[:, 0], dpts[:, 1],
  c=colors, edgecolors='k', s=120, zorder=3,
)
for w, c in zip(dir_words, colors):
  ax.annotate(
    w, dmap[w],
    xytext=(5, 3), textcoords='offset points',
    fontsize=9, color=c,
  )
# Arrows: man→woman and king→queen show parallel shift
for src, dst in [('man', 'woman'), ('king', 'queen')]:
  ax.annotate(
    '', xy=dmap[dst], xytext=dmap[src],
    arrowprops=dict(
      arrowstyle='->', color='gray', lw=1.5,
    ),
  )
ax.set_title("(3) Concept Direction: king − man + woman")
ax.grid(True, alpha=0.3)

# ─── Panel (1,0): Similarity bar chart ─────────────────────
ax = axs[1, 0]
pairs = [
  ('king', 'queen'),
  ('man', 'woman'),
  ('dog', 'cat'),
  ('tower', 'skyscraper'),
  ('apple', 'bicycle'),
]
labels = [f"{a} / {b}" for a, b in pairs]
scores = [model.similarity(a, b) for a, b in pairs]
colors_bar = [
  'steelblue' if s > 0.5 else 'salmon' for s in scores
]
ax.barh(labels, scores, color=colors_bar, edgecolor='k')
ax.set_xlim(0, 1)
ax.axvline(0.5, color='gray', linestyle='--', linewidth=0.8)
ax.set_title("(4) Similarity (cosine)")
ax.grid(True, alpha=0.3, axis='x')

# ─── Panel (1,1): Nearest Neighbors (Attention proxy) ──────
ax = axs[1, 1]
ax.axis('off')
query_words = ['neural', 'computer', 'king']
lines = ["Top-5 nearest neighbors\n"]
for qw in query_words:
  neighbors = model.most_similar(qw, topn=5)
  nb_str = ', '.join(w for w, _ in neighbors)
  lines.append(f"'{qw}':\n  {nb_str}\n")
ax.text(
  0.05, 0.95, ''.join(lines),
  transform=ax.transAxes,
  va='top', fontsize=8, family='monospace',
  wrap=True,
)
ax.set_title("(5) Nearest Neighbors")

# ─── Panel (1,2): Concept Direction result ─────────────────
ax = axs[1, 2]
ax.axis('off')
analogies = model.most_similar(
  positive=['king', 'woman'], negative=['man'], topn=5,
)
result_lines = [
  "king − man + woman ≈ ?\n\n",
  "Top-5 results:\n",
]
for rank, (word, score) in enumerate(analogies, 1):
  result_lines.append(f"  {rank}. {word:12s} ({score:.3f})\n")
ax.text(
  0.05, 0.95, ''.join(result_lines),
  transform=ax.transAxes,
  va='top', fontsize=9, family='monospace',
)
ax.set_title("(6) Concept Direction Result")

plt.suptitle(
  "GloVe 50-dim Word Embedding Visualizations",
  fontsize=13,
)
# rect leaves headroom at top so suptitle doesn't overlap panels
plt.tight_layout(rect=[0, 0, 1, 0.95])

_b = matplotlib.get_backend().lower()
if _b == 'agg':
  plt.savefig("embedding_map.png", bbox_inches='tight')
  print("Saved: embedding_map.png")
elif 'webagg' in _b:
  _port = matplotlib.rcParams.get('webagg.port', 8988)
  print(f"Open in browser: http://127.0.0.1:{_port}")
  print("Press Ctrl+C to exit.")
  plt.show()
else:
  plt.show()

# %%
