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

# %%
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


# %%
def plot_sin_n_theta(n, points=1000):
  theta = np.linspace(0, 2*np.pi, points)
  r = np.sin(n*theta)
  ax = plt.subplot(projection='polar')
  theta[r<0] += np.pi
  r = np.abs(r)
  ax.plot(theta, r)
  ax.set_title(f"r = sin({n}θ)")
  plt.show()

plot_sin_n_theta(5)


# %%
def plot_many(ns, points=1000):
  import math
  cols = min(len(ns), 4)
  rows = math.ceil(len(ns)/cols)
  fig, axs = plt.subplots(rows, cols, figsize=(4*cols, 4*rows),
                          subplot_kw={'projection': 'polar'})
  axs = np.array(axs).reshape(-1)
  for ax, n in zip(axs, ns):
    theta = np.linspace(0, 2*np.pi, points)
    r = np.sin(n*theta)
    theta[r<0] += np.pi
    r = np.abs(r)
    ax.plot(theta, r)
    ax.set_title(f"n={n}")
  # hide any unused axes
  for ax in axs[len(ns):]:
    ax.axis('off')
  plt.tight_layout()
  plt.show()

plot_many([1,2,3,4,5,6])


# %%
