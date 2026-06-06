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
    raise NotImplementedError

  # ------------------------------------------------------------------ #
  # Stack operations                                                     #
  # ------------------------------------------------------------------ #

  def push(self, disc: Disc) -> None:
    """Place a disc on top of this tower.

    Raises:
      ValueError: If the disc is larger than the current top disc
            (would violate the game rules).
    """
    raise NotImplementedError

  def pop(self) -> Disc:
    """Remove and return the top disc.

    Raises:
      IndexError: If the tower is empty.
    """
    raise NotImplementedError

  def peek(self) -> Disc | None:
    """Return the top disc without removing it, or None if empty."""
    raise NotImplementedError

  def is_empty(self) -> bool:
    """Return True if there are no discs on this tower."""
    raise NotImplementedError

  def size(self) -> int:
    """Return the number of discs currently on this tower."""
    raise NotImplementedError

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
    raise NotImplementedError

  # ------------------------------------------------------------------ #
  # Display                                                              #
  # ------------------------------------------------------------------ #

  def display(self) -> None:
    """Print this tower's current state to stdout using AsciiRenderer.

    Hint: build a single-tower state dict and call renderer.render().
    """
    raise NotImplementedError

  def __repr__(self) -> str:
    raise NotImplementedError
