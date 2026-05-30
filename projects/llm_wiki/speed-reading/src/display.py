"""display.py — PhaseDisplay: 3-column waterfall renderer.

Tracks 5 main phases (sanitizer→setup→converter→Seth→validator)
and 3 validator sub-steps (Leo→Quinn→Sentinel), then prints the
waterfall table at each phase transition.
"""
import sys

# Tree prefix per display level (5-char indentation step).
# L0=sanitizer L1=setup L2=converter L3=Seth
# L4=validator L5=Leo  L6=Quinn    L7=Sentinel
_PFX = (
  "",
  "└─ ",
  "     └─ ",
  "          └─ ",
  "               └─ ",
  "                    └─ ",
  "                         └─ ",
  "                              └─ ",
)
_VL_CONN = "                    |  "


def _mark(state: str) -> str:
  """Return status symbol for the given phase state."""
  return {
    "done":   "[✓]",
    "active": "[⟳]",
    "skip":   "[~]",
  }.get(state, "[ ]")


def _ptree(level: int, state: str, name: str) -> str:
  """Build phase-tree string padded to 45 display cols.

  Python len() counts Unicode code points which equals display
  cols for these chars — no byte-offset compensation needed.
  """
  cell = f"{_PFX[level]}{_mark(state)} {name}"
  return cell + " " * max(0, 45 - len(cell))


class PhaseDisplay:
  """Tracks phase/sub-phase states and renders the waterfall."""

  def __init__(self) -> None:
    # 5 main phases: sanitizer setup converter seth validator
    self.ph: list[str] = ["pending"] * 5
    # 3 validator sub-steps: leo quinn sentinel
    self.vl: list[str] = ["pending"] * 3
    self.vl_attempt: int = 0
    self.vl_max: int = 0
    self._book: str = "<book>"

  def set_book(self, name: str) -> None:
    self._book = name

  def waterfall(self) -> None:
    """Print the full 3-column waterfall to stdout."""
    b = self._book
    print()
    print(f"{'Phase':<45}  {'Function':<22}  Artifact")
    print(f"{'─' * 45}  {'─' * 22}  {'─' * 34}")
    self._row(0, self.ph[0], "sanitizer", "arg parser", "n/a")
    self._row(1, self.ph[1], "setup", "tool checker", "n/a")
    self._row(
      2, self.ph[2], "converter", "note taker",
      f".tmp/{b}-detailed-notes.md",
    )
    self._row(
      3, self.ph[3], "Seth", "synthesizer",
      f".tmp/{b}-mindmap-content.json",
    )
    print(
      f"{_ptree(4, self.ph[4], 'validator')}"
      f"  {'loop until success':<22}"
    )
    conn_sfx = (
      f"  (attempt {self.vl_attempt} of {self.vl_max})"
      if self.vl_attempt > 0 else ""
    )
    print(f"{_VL_CONN}Leo · Quinn · Sentinel{conn_sfx}")
    self._row(
      5, self.vl[0], "Leo", "map creator",
      f".tmp/{b}-mindmap.html",
    )
    self._row(6, self.vl[1], "Quinn", "QA reviewer", "qa")
    self._row(7, self.vl[2], "Sentinel", "final gate", "qa")
    print()

  def _row(
    self,
    level: int,
    state: str,
    name: str,
    func: str,
    artifact: str,
  ) -> None:
    print(
      f"{_ptree(level, state, name)}"
      f"  {func:<22}  {artifact}"
    )
