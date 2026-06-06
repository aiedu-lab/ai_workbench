"""
tower.py — Tower class.

Manages the ordered stack of discs on a single peg and knows how to
render itself via AsciiRenderer.
"""

from __future__ import annotations

from disc import Disc
from ascii_renderer import AsciiRenderer


class Tower:
  """Represents one peg in the Tower of Hanoi puzzle.

  Internally the tower is a stack: index 0 = bottom (largest disc),
  last index = top (smallest disc, next to be moved).

  Args:
    index     (int):       Which tower this is — 0, 1, or 2.
    num_discs (int):       Total number of discs in the puzzle
                 (needed so AsciiRenderer can size columns).
    discs     (list[Disc]): Initial discs, ordered bottom → top.
                 Pass an empty list for an empty tower.
  """

  def __init__(
    self,
    index: int,
    num_discs: int,
    discs: list[Disc] | None = None,
  ) -> None:
    self._index = index
    self._num_discs = num_discs
    self._discs: list[Disc] = list(discs) if discs else []
    self._renderer = AsciiRenderer(num_discs)

  # ------------------------------------------------------------------ #
  # Stack operations                                                     #
  # ------------------------------------------------------------------ #

  def push(self, disc: Disc) -> None:
    """Place a disc on top of this tower.

    Raises:
      ValueError: If the disc is larger than the current top disc
            (would violate the game rules).
    """
    top = self.peek()
    if top is not None and top < disc:
      raise ValueError(
        f"Cannot place {disc!r} on {top!r} — larger on smaller"
      )
    self._discs.append(disc)

  def pop(self) -> Disc:
    """Remove and return the top disc.

    Raises:
      IndexError: If the tower is empty.
    """
    if self.is_empty():
      raise IndexError("pop from empty tower")
    return self._discs.pop()

  def peek(self) -> Disc | None:
    """Return the top disc without removing it, or None if empty."""
    return self._discs[-1] if self._discs else None

  def is_empty(self) -> bool:
    """Return True if there are no discs on this tower."""
    return len(self._discs) == 0

  def size(self) -> int:
    """Return the number of discs currently on this tower."""
    return len(self._discs)

  # ------------------------------------------------------------------ #
  # State snapshot — used by AsciiRenderer and StepWriter               #
  # ------------------------------------------------------------------ #

  def as_size_list(self) -> list[int]:
    """Return disc sizes as a list ordered bottom → top.

    Example (three discs, all on tower):
      [3, 2, 1]
    Example (empty tower):
      []

    AsciiRenderer.render() expects a dict of these lists keyed by
    tower index:
      state = {0: tower0.as_size_list(),
           1: tower1.as_size_list(),
           2: tower2.as_size_list()}
    """
    return [d.size for d in self._discs]

  # ------------------------------------------------------------------ #
  # Display                                                              #
  # ------------------------------------------------------------------ #

  def display(self) -> None:
    """Print this tower's current state to stdout using AsciiRenderer.

    Hint: build a single-tower state dict and call renderer.render().
    """
    state = {self._index: self.as_size_list()}
    print(self._renderer.render(state))

  def __repr__(self) -> str:
    return f"Tower({self._index}, {self.as_size_list()})"
