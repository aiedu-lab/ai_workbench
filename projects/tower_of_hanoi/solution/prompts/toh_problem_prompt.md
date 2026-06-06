# Prompt: Tower of Hanoi — Problem Definition & Architecture

> **Teaching note:** This prompt is an example of a well-structured
> engineering prompt. Each section has a single job: *Context*
> establishes who and what, *Objective* defines the deliverables,
> *Constraints* bound the solution space, and *Output* specifies
> the exact shape of what is returned.

---

## Context

- **Language:** Python 3.12+ | **Test framework:** pytest
- **Audience:** Students learning OOP and recursion; they
  implement skeletons, not design them from scratch.
- **Provided utilities:** `AsciiRenderer` and `StepWriter` are
  fully implemented. Students call them; they do not write them.

---

## Objective

Generate a Python scaffold for a Tower of Hanoi solver:

1. **Four skeleton classes** (students implement):
   - `Disc` — immutable value object; comparable by size.
   - `Tower` — ordered stack that enforces the game rule:
     no disc may be placed on a smaller one.
   - `Move` — owns the recursive Hanoi algorithm; exposes it
     one step at a time via a `next() → bool` iterator.
   - `Orchestrator` — wires towers, `Move`, and `StepWriter`;
     drives the puzzle from initial state to completion.

2. **Two provided utilities** (fully implemented, not skeletons):
   - `AsciiRenderer` — renders the current tower state as a
     fixed-width ASCII diagram; input is a dict mapping tower
     index to a list of disc sizes ordered bottom → top.
   - `StepWriter` — appends each move as a `## Step N` Markdown
     section with a fenced ASCII-art block to an output file;
     supports `echo_to_stdout` and the context-manager protocol.

3. **A CLI entry point** (`main.py`) with `--number-discs`,
   `--step-by-step` / `--no-step-by-step`, and `--step-file`.
   When `step_by_step=True`, display ASCII art after each move
   and pause for Enter.

4. **A README.md** explaining the game rules, the recursive
   solution, and how to run the CLI.

---

## Solution Approach

`Move._hanoi(n, source, target, spare)` — private recursive method:

1. Move top N−1 discs: `source → spare`
2. Move bottom disc: `source → target`
3. Move N−1 discs: `spare → target`

Boundary: N = 0 → do nothing.  Minimum moves: **2ᴺ − 1**.

---

## Style Rules

- Python 3.12+ modern constructs: `list[X]`, `dict[K,V]`,
  `T | None` — never import from `typing`
- Keyword arguments for constructors with more than one argument

---

## Output

Return one file per bullet; all Python lives under `src/`:

- `README.md`
- `src/disc.py`  `src/tower.py`  `src/move.py`
  `src/orchestrator.py`
- `src/ascii_renderer.py`  `src/step_writer.py`
  *(fully implemented — not skeletons)*
- `src/main.py`

Every skeleton body: exactly `raise NotImplementedError`.

### Student Workflow

`src/` is the pristine scaffold committed to the repo.
Students copy it to begin work (`src_copy/` is git-ignored):

```bash
cp -r src src_copy
```

Apply `solution/prompts/toh_complete_solution_prompt.md` via
Claude CLI to fill in the skeletons in `src_copy/`.
