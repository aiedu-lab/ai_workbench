# Prompt: Tower of Hanoi — Python Exercise Scaffold

> **Teaching note:** This prompt is an example of a well-structured engineering prompt.
> Notice how each section has a single job: *Context* establishes who and what,
> *Objective* defines the deliverables, *Constraints* bound the solution space, and
> *Output* specifies the exact shape of what is returned.
> Ambiguities that were left out (e.g. "just give me ASCII art I can use") force
> clarifying rounds — everything below was learned from exactly that conversation.

---

## Context

- **Language:** Python 3.12+
- **Test framework:** pytest
- **Audience:** Students learning OOP and recursion; they will *implement* the
  skeletons, not design them from scratch.
- **Provided utilities:** `AsciiRenderer` and `StepWriter` are **fully implemented**
  and handed to students as black-box helpers. Students call them; they do not write
  them. This removes the ASCII-art distraction so students can focus on the algorithm
  and class design.

---

## Objective

Generate a complete Python project scaffold for the **Tower of Hanoi** exercise.
The scaffold must include:

1. A `README.md` explaining the rules and the recursive solution.
2. Four skeleton classes with documented public interfaces and `raise NotImplementedError` bodies.
3. Two fully implemented utility classes students use as-is.
4. A CLI entry point (`main.py`).
5. A pytest test suite with one test file per class plus an integration test file.

---

## Constraints

### README.md
- State the three game rules concisely (one peg at a time, no larger on smaller, goal is Tower[2]).
- Explain the recursive solution in three steps:
  1. Move top N−1 discs from `Tower[0]` → `Tower[1]` (using `Tower[2]` as spare).
  2. Move the remaining bottom disc from `Tower[0]` → `Tower[2]`.
  3. Move the N−1 discs from `Tower[1]` → `Tower[2]` (using `Tower[0]` as spare).
- State the boundary condition: when N = 1, move directly from source to target.
- Show the `AsciiRenderer` call signature and a labelled sample output so students know
  exactly what to pass and what to expect — **no implementation required from them**.
- Show the project directory tree and the two `python main.py` invocation examples.

### Disc (value object)
- Immutable; carries a single `size: int` attribute.
- Constructor raises `ValueError` for non-positive sizes.
- Supports `==` and `<` so Tower can enforce ordering rules.

### Tower
- Constructor: `Tower(index, num_discs, discs=[])` — `num_discs` is needed to size
  the renderer column correctly.
- Stack operations: `push(disc)`, `pop()`, `peek()`, `is_empty()`, `size()`.
- `push()` must raise `ValueError` when placing a larger disc on a smaller one.
- `as_size_list() → list[int]` returns disc sizes ordered **bottom → top**; this is
  the format `AsciiRenderer.render()` expects.
- `display()` prints the current state to stdout via `AsciiRenderer`; students call
  this during interactive mode.

### Move
- Constructor: `Move(towers, num_discs, step_by_step, step_writer)`.
- `next() → bool`: executes one move; returns `True` if a move was made, `False` if
  already solved (final state: Tower[2] holds all discs in order).
- `write_step(step_number, from_tower, to_tower)`: delegates to `StepWriter`; called
  internally by `next()`.
- `is_solved() → bool`: public predicate for tests and Orchestrator.
- `_hanoi(n, source, target, spare)`: **private** recursive method; students implement
  the three-step recursion here. Keeping it private signals that callers use `next()`,
  not the recursion directly.

### Orchestrator
- Constructor: `Orchestrator(num_discs, step_by_step, step_file)`.
- `run()`: loops `move.next()` until it returns `False`; closes `StepWriter` on exit.
- `get_towers() → list[Tower]` and `get_move() → Move`: accessors for test inspection
  without exposing internals directly.

### AsciiRenderer (fully implemented — do not skeleton)
- `AsciiRenderer(num_discs)` then `render(state: dict[int, list[int]]) → str`.
- `state` keys are tower indices 0/1/2; values are size lists ordered bottom → top.
- Disc tokens are proportional to size; columns are fixed-width so the diagram never
  reflows as discs move.
- Include a labelled sample for 3 discs in the README (towers header, disc rows, `===`
  ground line, index footer).

### StepWriter (fully implemented — do not skeleton)
- `StepWriter(step_file, echo_to_stdout=False)`.
- `write(step_number, from_tower, to_tower, ascii_art)`: appends a `## Step N` section
  with a fenced code block to the Markdown file.
- `write_initial(ascii_art)`: writes the board state before any moves.
- `close()`: flushes and finalises the file (appends "Puzzle solved!" footer).
- Supports context-manager protocol (`with StepWriter(...) as w:`).

### main.py
- First line must be `#!/usr/bin/env python3`.
- Uses `argparse` with:
  - `--number-discs` (int, default 3)
  - `--step-by-step` / `--no-step-by-step` (bool, default `True`)
    — when `True`, `display()` is called after each move and the
    loop waits for Enter.
  - `--step-file` (str, default `"./steps_filename.md"`)
- Validates that `--number-discs ≥ 1`; exits with a clear error
  otherwise.
- `main()` constructs `Orchestrator` and calls `run()`.
- Entry guard: `sys.exit(main())` (not bare `main()`).
- Run commands:
  ```bash
  python3 src/main.py <num_discs>
  python3 src/main.py <num_discs> --no-step-by-step
  ```

### Style Rules
- Line length ≤ 80 columns.
- 2-space indentation throughout.
- Python 3.12+ types only: `list[X]`, `dict[K, V]`, `T | None`.
  Never import from `typing`.
- Use `object` (not `Any`) for truly unknown types.
- Always use named (keyword) parameters when calling constructors
  with more than one argument.

### Test suite
- One file per class: `test_disc.py`, `test_tower.py`, `test_move.py`,
  `test_orchestrator.py`, plus `test_integration.py`.
- `tests/conftest.py` adds the project root to `sys.path` so `pytest tests/` works
  without packaging.
- Every test class name follows the `TestXxxYyy` convention.
- All test bodies contain `raise NotImplementedError` or an `assert` with a clear
  intent comment — no empty `pass` bodies.
- **Required test cases per file:**

  | File | Must cover |
  |---|---|
  | `test_disc.py` | valid construction, zero/negative raises `ValueError`, `==`, `<` |
  | `test_tower.py` | empty/full construction, `peek` (non-destructive), `pop` on empty raises, illegal `push` raises, `as_size_list` correctness, `display` produces output |
  | `test_move.py` | `is_solved` false at start, `next` returns `True` while moves remain, `next` returns `False` when done, Tower[2] has all discs after completion, move count equals 2ᴺ − 1 |
  | `test_orchestrator.py` | initial tower state, all three post-run assertions (Tower[2] full, Tower[0]/[1] empty), step file created and non-empty, move count via file heading count |
  | `test_integration.py` | parametrized N=1,2,3; correct final state; correct move count; **ordering invariant** — assert no tower ever has a larger disc above a smaller one at any intermediate step |

---

## Output

Return **one file per bullet** with no additional prose between them.
All Python source files live under `src/`:

- `README.md`
- `src/disc.py`
- `src/tower.py`
- `src/move.py`
- `src/orchestrator.py`
- `src/ascii_renderer.py` *(fully implemented)*
- `src/step_writer.py` *(fully implemented)*
- `src/main.py`
- `src/tests/conftest.py`
- `src/tests/test_disc.py`
- `src/tests/test_tower.py`
- `src/tests/test_move.py`
- `src/tests/test_orchestrator.py`
- `src/tests/test_integration.py`

Every skeleton method body must be exactly `raise NotImplementedError` — no hints,
no placeholder logic. Docstrings are the only guidance students receive.
