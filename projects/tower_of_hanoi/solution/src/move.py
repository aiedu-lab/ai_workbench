"""
move.py — Move class.

Generates the recursive sequence of moves and publishes each step
either to stdout (step-by-step) or to a Markdown file.
"""

from __future__ import annotations

from tower import Tower
from step_writer import StepWriter
from ascii_renderer import AsciiRenderer


class Move:
  """Generates and executes the complete move sequence for the puzzle.

  The Move class owns the recursion.  It maintains an internal iterator
  over all legal moves so that callers can advance one step at a time
  via ``next()``.

  Args:
    towers      (list[Tower]):  The three Tower objects
                  [Tower0, Tower1, Tower2].
    num_discs   (int):          Total discs in the puzzle.
    step_by_step (bool):        If True, ``next()`` pauses for
                  user input after rendering.
                  If False, just records the step.
    step_writer (StepWriter):   Helper that writes Markdown
                  output to a file.
  """

  def __init__(
    self,
    towers: list[Tower],
    num_discs: int,
    step_by_step: bool,
    step_writer: StepWriter,
  ) -> None:
    self._towers = towers
    self._num_discs = num_discs
    self._step_by_step = step_by_step
    self._step_writer = step_writer
    self._renderer = AsciiRenderer(num_discs)
    self._step_count = 0
    # Pre-compute the full move sequence at construction time.
    self._queue: list[tuple[int, int]] = []
    self._hanoi(num_discs, 0, 2, 1)

  # ------------------------------------------------------------------ #
  # Public interface                                                     #
  # ------------------------------------------------------------------ #

  def next(self) -> bool:
    """Execute the next legal move.

    - Moves the appropriate disc between towers.
    - Calls ``write_step()`` to record / display the new state.
    - If ``step_by_step`` is True, waits for the user to press Enter.

    Returns:
      True  — a move was made; more moves may remain.
      False — the puzzle is already in its final state (Tower[2] holds
          all discs in order); no move was made.
    """
    if not self._queue:
      return False
    source, target = self._queue.pop(0)
    disc = self._towers[source].pop()
    self._towers[target].push(disc)
    self._step_count += 1
    self.write_step(self._step_count, source, target)
    if self._step_by_step:
      input("Press Enter to continue...")
    return True

  def write_step(
    self,
    step_number: int,
    from_tower: int,
    to_tower: int,
  ) -> None:
    """Record the current board state as one step.

    Builds a state snapshot from the towers and delegates to
    ``StepWriter.write()`` so output format is consistent whether
    writing to a file or stdout.

    Args:
      step_number: 1-based step counter.
      from_tower:  Index of the tower the disc was moved FROM.
      to_tower:    Index of the tower the disc was moved TO.
    """
    state = {i: t.as_size_list() for i, t in enumerate(self._towers)}
    ascii_art = self._renderer.render(state)
    self._step_writer.write(step_number, from_tower, to_tower, ascii_art)

  def is_solved(self) -> bool:
    """Return True if Tower[2] holds all discs in correct order."""
    expected = list(range(self._num_discs, 0, -1))
    return self._towers[2].as_size_list() == expected

  # ------------------------------------------------------------------ #
  # Private helpers                                                      #
  # ------------------------------------------------------------------ #

  def _hanoi(self, n: int, source: int, target: int, spare: int) -> None:
    """Core recursive algorithm.  Yields moves into an internal queue.

    Students implement the three-step recursion described in README.md.

    Args:
      n:      Number of discs to move.
      source: Index of the source tower.
      target: Index of the destination tower.
      spare:  Index of the intermediate/spare tower.
    """
    if n == 0:
      return
    self._hanoi(n - 1, source, spare, target)
    self._queue.append((source, target))
    self._hanoi(n - 1, spare, target, source)
