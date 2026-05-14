# Python Virtual Environment Setup

Covers creating an isolated Python environment with
[pip-tools](https://pip-tools.readthedocs.io/) for
reproducible dependency management and registering a Jupyter
kernel for VS Code / JupyterLab cell-by-cell execution.

Used by: [Embeddings Visualization](
../../sessions/embedding.md) and any project with a
`requirements.in` file.

---

## Create and Activate the Environment

```bash
cd projects/embedding          # or any project directory
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux / WSL2
# Windows (PowerShell): .venv\Scripts\Activate.ps1
```

---

## Install Dependencies with pip-tools

```bash
pip install pip-tools

# Compile: resolves and pins all transitive dependencies
pip-compile requirements.in

# Sync: installs exactly what is in requirements.txt
# and removes anything else
pip-sync requirements.txt
```

> `requirements.txt` is generated — do not edit it by hand.
> To add a package, append it to `requirements.in` and
> re-run `pip-compile && pip-sync`.

---

## Register the Jupyter Kernel

So VS Code and JupyterLab can see the `.venv` environment:

```bash
python3 -m ipykernel install --user --name .venv \
  --display-name "Python3 (.venv)"
```

**VS Code:** open a `# %%`-annotated `.py` file; VS Code
detects Jupyter cells and shows **Run Cell** buttons. Select
the `Python3 (.venv)` kernel when prompted.

**JupyterLab:** run `jupyter lab` from the project directory,
then select the `Python3 (.venv)` kernel for your notebook.

---

## Validation

Verify the environment is ready:

```bash
source projects/embedding/.venv/bin/activate
python3 -c "import gensim, sklearn, matplotlib; print('OK')"
```

Expected: `OK` printed without errors.

For the Embeddings project specifically:

```bash
cd projects/embedding
# WSL2: set BROWSER so WebAgg can open the browser window
export BROWSER='/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'
python3 embed.py
```

Expected: a 2×3 panel figure opens in the browser (WebAgg)
or saves as `embedding_map.png` (Agg fallback).

> First run downloads the GloVe model (~65 MB) and caches
> it as `glove_50.bin` inside the project directory
> (gitignored). Subsequent runs load from cache in seconds.
