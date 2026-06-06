# Solution Prompt: Tower of Hanoi — Implement Skeleton Classes

You are working in `projects/tower_of_hanoi/src_copy/`.
This directory is a copy of the student scaffold.  Four files
have skeleton methods that each `raise NotImplementedError`.
Two utility files (`ascii_renderer.py`, `step_writer.py`) are
fully implemented — do not modify them.

Implement the four skeleton classes one at a time, running the
corresponding tests after each to confirm correctness before
moving on.

## Steps

1. Read `disc.py`.  Implement all methods.
   Run `python -m pytest tests/test_disc.py -v` to verify.

2. Read `tower.py`.  Implement all methods.
   Run `python -m pytest tests/test_tower.py -v` to verify.

3. Read `move.py`.  Implement all methods.
   The `_hanoi` helper owns the recursion; `next()` executes
   one move at a time from a pre-computed queue.
   Run `python -m pytest tests/test_move.py -v` to verify.

4. Read `orchestrator.py`.  Implement all methods.
   Run `python -m pytest tests/test_orchestrator.py
   tests/test_integration.py -v` to verify.

Fix any test failures before proceeding to the next class.
All tests must pass by the end of step 4.

## Constraints

- 2-space indentation; line length ≤ 79 characters.
- Python 3.12+ types (`list[X]`, `T | None`).
  Never import from `typing`.
- Do not modify tests, `ascii_renderer.py`, `step_writer.py`,
  `main.py`, or `conftest.py`.
