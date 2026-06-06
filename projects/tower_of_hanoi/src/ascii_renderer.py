"""
ascii_renderer.py — PROVIDED UTILITY. Students do not need to modify this file.

Renders the current state of all three towers as a fixed-width ASCII string.

Usage:
  renderer = AsciiRenderer(num_discs=3)
  state    = {0: [3, 2, 1], 1: [], 2: []}   # bottom → top per tower
  print(renderer.render(state))
"""

from __future__ import annotations


class AsciiRenderer:
  """Converts a tower-state dict into a printable ASCII string.

  Args:
    num_discs (int): Total number of discs in the puzzle.  This fixes
             the column width so the diagram never reflows.
  """

  # Width of the widest disc bracket pair, e.g. "[  3  ]" for size 3
  _PEG_CHAR = "|"
  _COL_GAP = 6  # spaces between columns

  def __init__(self, num_discs: int) -> None:
    if num_discs < 1:
      raise ValueError("num_discs must be >= 1")
    self._num_discs = num_discs
    # Max disc token width: "[ N ]" where N is padded to `num_discs` chars
    self._disc_width = num_discs * 2 + 3   # brackets + spaces + digit(s)
    self._col_width = max(self._disc_width, len("Tower[0]"))

  # ------------------------------------------------------------------ #
  # Public                                                               #
  # ------------------------------------------------------------------ #

  def render(self, state: dict[int, list[int]]) -> str:
    """Return a multi-line ASCII string showing all three towers.

    Args:
      state: Mapping of tower index (0/1/2) to a list of disc sizes
           ordered **bottom → top**.  Missing keys are treated as
           empty towers.

    Returns:
      A plain string ready to be printed or written to a file.
    """
    towers = [state.get(i, []) for i in range(3)]
    lines: list[str] = []

    # Header
    lines.append(self._header_row())
    lines.append("")

    # Rows from top of diagram down to ground
    for row in range(self._num_discs, 0, -1):
      cells = []
      for t in range(3):
        stack = towers[t]
        # How many discs are on this tower?
        disc_index = len(stack) - (self._num_discs - row + 1)
        if disc_index >= 0 and disc_index < len(stack):
          # There IS a disc at this row height
          size = stack[disc_index]
          cells.append(self._disc_token(size))
        else:
          cells.append(self._peg_token())
      lines.append(self._join_cells(cells))

    # Ground line
    total_width = self._col_width * 3 + self._COL_GAP * 2
    lines.append("=" * total_width)

    # Footer indices
    lines.append(self._footer_row())
    return "\n".join(lines)

  # ------------------------------------------------------------------ #
  # Private helpers                                                      #
  # ------------------------------------------------------------------ #

  def _header_row(self) -> str:
    labels = [f"Tower[{i}]" for i in range(3)]
    return self._join_cells([l.center(self._col_width) for l in labels])

  def _footer_row(self) -> str:
    indices = [str(i) for i in range(3)]
    return self._join_cells([i.center(self._col_width) for i in indices])

  def _peg_token(self) -> str:
    return self._PEG_CHAR.center(self._col_width)

  def _disc_token(self, size: int) -> str:
    # e.g. size=2, num_discs=3 → "[ 2 ]" padded to col_width
    inner = " " * (size - 1) + str(size) + " " * (size - 1)
    token = f"[{inner}]"
    return token.center(self._col_width)

  @staticmethod
  def _join_cells(cells: list[str]) -> str:
    gap = " " * AsciiRenderer._COL_GAP
    return gap.join(cells)
