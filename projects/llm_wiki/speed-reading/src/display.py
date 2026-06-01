"""display.py — PhaseDisplay: 3-column waterfall renderer.

Tracks 5 main phases (sanitizer→setup→converter→Seth→validator)
and 3 validator sub-steps (Leo→Quinn→Sentinel), then prints the
waterfall table at each phase transition.
"""
import io

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

  def __init__(self, log_path: str | None = None) -> None:
    # 5 main phases: sanitizer setup converter seth validator
    self.ph: list[str] = ["pending"] * 5
    # 3 validator sub-steps: leo quinn sentinel
    self.vl: list[str] = ["pending"] * 3
    self.vl_attempt: int = 0
    self.vl_max: int = 0
    self._book: str = "<book>"
    # Append each waterfall snapshot here when set; readable
    # via `tail` even when stdout is unavailable (agent spawn).
    self._log_path: str | None = log_path

  def set_book(self, name: str) -> None:
    self._book = name

  def waterfall(self) -> None:
    """Print the waterfall to stdout; append snapshot to log."""
    b = self._book
    buf = io.StringIO()

    def emit(line: str = "") -> None:
      print(line)
      buf.write(line + "\n")

    emit()
    emit(f"{'Phase':<45}  {'Function':<22}  Artifact")
    emit(f"{'─' * 45}  {'─' * 22}  {'─' * 34}")
    self._emit_row(emit, 0, self.ph[0], "sanitizer",
                   "arg parser", "n/a")
    self._emit_row(emit, 1, self.ph[1], "setup",
                   "tool checker", "n/a")
    self._emit_row(emit, 2, self.ph[2], "converter",
                   "note taker",
                   f".tmp/{b}-detailed-notes.md")
    self._emit_row(emit, 3, self.ph[3], "Seth",
                   "synthesizer",
                   f".tmp/{b}-mindmap-content.json")
    vl_line = (
      f"{_ptree(4, self.ph[4], 'validator')}"
      f"  {'loop until success':<22}"
    )
    emit(vl_line)
    conn_sfx = (
      f"  (attempt {self.vl_attempt} of {self.vl_max})"
      if self.vl_attempt > 0 else ""
    )
    emit(f"{_VL_CONN}Leo · Quinn · Sentinel{conn_sfx}")
    sfx = f"-{self.vl_attempt}" if self.vl_attempt > 0 else ""
    self._emit_row(emit, 5, self.vl[0], "Leo",
                   "map creator",
                   f".tmp/{b}-mindmap{sfx}.html")
    self._emit_row(emit, 6, self.vl[1], "Quinn",
                   "QA reviewer", "qa")
    self._emit_row(emit, 7, self.vl[2], "Sentinel",
                   "final gate", "qa")
    emit()
    if self._log_path:
      with open(self._log_path, "a", encoding="utf-8") as lf:
        lf.write(buf.getvalue())

  def _emit_row(
    self,
    emit,
    level: int,
    state: str,
    name: str,
    func: str,
    artifact: str,
  ) -> None:
    emit(
      f"{_ptree(level, state, name)}"
      f"  {func:<22}  {artifact}"
    )
