"""
disc.py — Disc value object.

A Disc is immutable and identified solely by its size (a positive integer).
Larger size = larger disc. Students do not need to modify this class.
"""


class Disc:
  """Immutable value object representing a single disc.

  Attributes:
    size (int): Positive integer; larger value means a
          physically larger disc.
  """

  def __init__(self, size: int) -> None:
    """
    Args:
      size: Must be a positive integer.

    Raises:
      ValueError: If size is not a positive integer.
    """
    if not isinstance(size, int) or size <= 0:
      raise ValueError(f"size must be a positive integer, got {size!r}")
    self.size = size

  # ------------------------------------------------------------------ #
  # Comparison helpers — lets you write:  disc_a < disc_b               #
  # ------------------------------------------------------------------ #

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Disc):
      return NotImplemented
    return self.size == other.size

  def __lt__(self, other: "Disc") -> bool:
    return self.size < other.size

  def __repr__(self) -> str:
    return f"Disc({self.size})"
