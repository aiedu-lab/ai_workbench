# Tower of Hanoi

## Rules

1. There are **three towers** (`Tower[0]`, `Tower[1]`, `Tower[2]`) and **N discs** of distinct sizes.
2. All discs start stacked on `Tower[0]`, largest at the bottom, smallest at the top.
3. The goal is to move all discs to `Tower[2]` in the same order.
4. **Only one disc may be moved at a time** — always the top disc of a tower.
5. **A larger disc may never be placed on top of a smaller disc.**

---

## Recursive Solution

### Key Insight

To move **N discs** from a `source` tower to a `target` tower (using `spare` as intermediate):

1. Recursively move the top **N−1 discs** from `source → spare` (using `target` as the spare).
2. Move the single remaining (largest) disc from `source → target`.
3. Recursively move the **N−1 discs** from `spare → target` (using `source` as the spare).

### Boundary Condition

When **N = 1**: move the single disc directly from `source` to `target`. No recursion needed.

### Pseudocode

```
def hanoi(n, source, target, spare):
    if n == 1:
        move disc from source to target   # boundary condition
        return
    hanoi(n - 1, source, spare, target)   # step 1: free the bottom disc
    move disc from source to target        # step 2: move the largest disc
    hanoi(n - 1, spare, target, source)   # step 3: stack the rest on top
```

For **N discs** the minimum number of moves is **2ᴺ − 1**.

---

## ASCII Art Utility

You do **not** need to implement ASCII art yourself. Use the provided `AsciiRenderer` utility:

```python
from ascii_renderer import AsciiRenderer

renderer = AsciiRenderer(num_discs=3)

# Render current tower state to a string
state = {0: [3, 2, 1], 1: [], 2: []}   # lists of disc sizes, bottom → top
print(renderer.render(state))
```

### What the output looks like (3 discs)

```
Tower[0]          Tower[1]          Tower[2]
   |                  |                  |
  [1]                 |                  |
 [ 2 ]                |                  |
[  3  ]               |                  |
==========================================
   0                  1                  2
```

Each disc is drawn proportional to its size. The `render(state)` method returns a
plain string — print it, write it to a file, or embed it in Markdown as a fenced
code block (see `StepWriter` for the Markdown helper).

---

## Project Structure

```
tower_of_hanoi/
├── README.md
├── toh_prompt.md           # HDD spec given to AI
└── src/
    ├── main.py             # CLI entry point
    ├── orchestrator.py     # Orchestrator class
    ├── tower.py            # Tower class
    ├── move.py             # Move class
    ├── disc.py             # Disc value-object
    ├── ascii_renderer.py   # AsciiRenderer (provided)
    ├── step_writer.py      # StepWriter (provided)
    └── tests/
        ├── conftest.py
        ├── test_disc.py
        ├── test_tower.py
        ├── test_move.py
        ├── test_orchestrator.py
        └── test_integration.py
```

---

## Running

```bash
# Solve in one shot — prints all moves
python3 src/main.py 3

# Step through one move at a time (press Enter each step)
python3 src/main.py 3 --step-by-step

# Write all steps to a Markdown file silently
python3 src/main.py 4 --no-step-by-step \
  --step-file ./solution.md

# Defaults: 3 discs, step-by-step
python3 src/main.py
```

## Running Tests

```bash
pytest src/tests/
```
