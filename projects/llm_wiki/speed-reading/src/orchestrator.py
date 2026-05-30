"""orchestrator.py — Piper: book-to-mindmap pipeline orchestrator.

Sequences the five pipeline phases (sanitizer → setup →
converter → Seth → validator-loop) and implements the
coordination doctrine from agents/piper-pipeline-orchestrator.md:
task scope locking, agent sequencing, retry policy (up to 3),
and independent final verification via Sentinel.
"""
import shutil
import subprocess
import sys
from pathlib import Path

from display import PhaseDisplay
from spinner import Spinner

# Map phase name → numeric skip index.
_PHASE_IDX: dict[str, int] = {
  "sanitizer":      0,
  "setup":          1,
  "converter":      2,
  "seth":           3,
  "validator-loop": 4,
  "leo":            4,  # alias: start the full validator loop
  "quinn":          4,  # alias: start the full validator loop
  "sentinel":       4,  # alias: start the full validator loop
}
_VALID_EXT = {"pdf", "html", "htm", "txt", "md"}


class Piper:
  """Orchestrates the book-to-mindmap pipeline."""

  MAX_RETRIES = 3

  def __init__(
    self,
    input_path: str,
    output_path: str,
    from_phase: str,
  ) -> None:
    self._input = input_path
    self._from_idx = _PHASE_IDX[from_phase]
    self._script_dir = Path(__file__).resolve().parent.parent
    self._agent_dir = self._script_dir / "agents"
    self._display = PhaseDisplay()
    self._display.vl_max = self.MAX_RETRIES
    self._spinner = Spinner()
    # Resolved during sanitizer phase
    self._ext: str = ""
    self._is_url: bool = False
    self._abs_input: str = ""
    self._abs_output = Path(output_path)
    self._work_dir: Path = Path()
    self._notes_file: Path = Path()
    self._content_json: Path = Path()
    self._html_file: Path = Path()

  def run(self) -> int:
    """Run all phases in sequence; return process exit code."""
    self._display.ph[0] = "active"
    try:
      self._phase_sanitizer()
      self._phase_setup()
      self._phase_converter()
      self._phase_seth()
      self._phase_validator_loop()
    except SystemExit as exc:
      self._spinner.stop()
      return int(exc.code) if exc.code is not None else 1
    finally:
      self._spinner.stop()
    shutil.copy(str(self._html_file), str(self._abs_output))
    print(f"[done] Mindmap saved: {self._abs_output}")
    return 0

  # ── Phase: Argument Sanitizer ─────────────────────────────────

  def _phase_sanitizer(self) -> None:
    inp = self._input
    ext = inp.rsplit(".", 1)[-1].lower() if "." in inp else ""
    if ext not in _VALID_EXT:
      self._abort(
        f"Error: unsupported extension '.{ext}'.\n"
        f"  Supported: {' '.join(sorted(_VALID_EXT))}"
      )
    self._ext = ext
    self._is_url = inp.startswith(("http://", "https://"))
    if self._is_url:
      r = subprocess.run(
        ["curl", "-fsS", "--head", inp], capture_output=True
      )
      if r.returncode != 0:
        self._abort(f"Error: URL not reachable: {inp}")
      self._abs_input = inp
    else:
      p = Path(inp)
      if not p.is_file():
        self._abort(f"Error: file not found: {inp}")
      self._abs_input = str(p.resolve())
    base = Path(inp).name if not self._is_url else inp
    book_name = Path(base).stem
    self._display.set_book(book_name)
    self._resolve_paths(book_name)
    self._display.ph[0] = "done"
    for i in range(1, self._from_idx):
      self._display.ph[i] = "skip"
    self._display.waterfall()

  def _resolve_paths(self, book_name: str) -> None:
    out = self._abs_output
    out.parent.mkdir(parents=True, exist_ok=True)
    self._abs_output = out.parent.resolve() / out.name
    output_dir = self._abs_output.parent
    self._work_dir = output_dir / ".tmp"
    self._notes_file = (
      self._work_dir / f"{book_name}-detailed-notes.md"
    )
    self._content_json = (
      self._work_dir / f"{book_name}-mindmap-content.json"
    )
    self._html_file = (
      self._work_dir / f"{book_name}-mindmap.html"
    )

  # ── Phase: Utility Setup ──────────────────────────────────────

  def _phase_setup(self) -> None:
    if self._from_idx > 1:
      self._work_dir.mkdir(parents=True, exist_ok=True)
      return
    self._display.ph[1] = "active"
    self._display.waterfall()
    self._spinner.start("Checking required CLI tools...")
    try:
      self._check_tools()
      self._work_dir.mkdir(parents=True, exist_ok=True)
    finally:
      self._spinner.stop()
    self._display.ph[1] = "done"

  def _check_tools(self) -> None:
    ext = self._ext
    if ext == "pdf" and not shutil.which("pdftotext"):
      self._abort(
        "Error: pdftotext not found.\n"
        "  Install: sudo apt install poppler-utils"
      )
    if ext in ("html", "htm") and not shutil.which("html2text"):
      self._abort(
        "Error: html2text not found.\n"
        "  Install: sudo apt install html2text"
      )

  # ── Phase: File Converter ─────────────────────────────────────

  def _phase_converter(self) -> None:
    if self._from_idx > 2:
      self._require_artifact(self._notes_file)
      return
    self._display.ph[2] = "active"
    self._display.waterfall()
    label = Path(self._abs_input).name
    self._spinner.start(f"Converting {label} to plain text...")
    try:
      self._convert_input()
    finally:
      self._spinner.stop()
    self._display.ph[2] = "done"

  def _convert_input(self) -> None:
    ext, inp = self._ext, self._abs_input
    notes = str(self._notes_file)
    if ext == "pdf":
      subprocess.run(["pdftotext", inp, notes], check=True)
    elif ext in ("html", "htm") and self._is_url:
      curl = subprocess.run(
        ["curl", "-fsSL", inp],
        capture_output=True, check=True,
      )
      h2t = subprocess.run(
        ["html2text"], input=curl.stdout,
        capture_output=True, check=True,
      )
      self._notes_file.write_bytes(h2t.stdout)
    elif ext in ("html", "htm"):
      out = subprocess.run(
        ["html2text", inp], capture_output=True, check=True
      )
      self._notes_file.write_bytes(out.stdout)
    else:
      shutil.copy(inp, notes)

  # ── Phase: Seth Synthesizer ───────────────────────────────────

  def _phase_seth(self) -> None:
    if self._from_idx > 3:
      self._require_artifact(self._content_json)
      return
    self._display.ph[3] = "active"
    self._display.waterfall()
    self._spinner.start(
      "Seth · synthesising concepts → mindmap JSON..."
    )
    try:
      self._run_agent(
        f"Synthesize {self._notes_file}"
        f" into {self._content_json}",
        "seth-content-synthesizer.md",
        "Seth",
      )
    finally:
      self._spinner.stop()
    if not self._content_json.is_file():
      self._abort(
        f"Error: Seth did not produce {self._content_json}."
      )
    self._display.ph[3] = "done"

  # ── Phase: Validator Loop (Leo → Quinn → Sentinel) ────────────

  def _phase_validator_loop(self) -> None:
    self._display.ph[4] = "active"
    for attempt in range(1, self.MAX_RETRIES + 1):
      self._display.vl_attempt = attempt
      if self._validator_attempt(attempt):
        self._display.ph[4] = "done"
        return
    self._abort("Error: max retries reached.")

  def _validator_attempt(self, attempt: int) -> bool:
    """Run one Leo→Quinn→Sentinel cycle. True if approved."""
    self._display.vl = ["active", "pending", "pending"]
    self._display.waterfall()
    self._run_leo()
    self._display.vl = ["done", "active", "pending"]
    self._display.waterfall()
    quinn_out = self._run_quinn()
    if "NOT APPROVED" in quinn_out:
      self._display.vl = ["done", "skip", "skip"]
      if attempt >= self.MAX_RETRIES:
        self._display.ph[4] = "active"
        self._display.waterfall()
        self._abort(
          "Error: Quinn NOT APPROVED — max retries.\n"
          + quinn_out
        )
      self._display.waterfall()
      return False
    self._display.vl = ["done", "done", "active"]
    self._display.waterfall()
    sent_out = self._run_sentinel()
    if "NOT APPROVED" in sent_out:
      self._display.vl = ["done", "done", "skip"]
      if attempt >= self.MAX_RETRIES:
        self._display.ph[4] = "active"
        self._display.waterfall()
        self._abort(
          "Error: Sentinel NOT APPROVED — max retries.\n"
          + sent_out
        )
      self._display.waterfall()
      return False
    self._display.vl = ["done", "done", "done"]
    return True

  def _run_leo(self) -> None:
    self._spinner.start(
      "Leo · rendering vis-network mindmap HTML..."
    )
    try:
      self._run_agent(
        f"Render {self._content_json} into {self._html_file}",
        "leo-layout-engineer.md",
        "Leo",
      )
    finally:
      self._spinner.stop()

  def _run_quinn(self) -> str:
    self._spinner.start(
      "Quinn · reviewing layout, hierarchy, content..."
    )
    try:
      return self._run_agent(
        f"Review {self._html_file} for quality issues.",
        "quinn-qa-reviewer.md",
        "Quinn",
      )
    finally:
      self._spinner.stop()

  def _run_sentinel(self) -> str:
    self._spinner.start(
      "Sentinel · final guard: spacing, completeness..."
    )
    try:
      return self._run_agent(
        f"Final verification of {self._html_file}."
        " Quinn approved. Independently verify"
        " — overrule if you see any failure.",
        "sentinel-final-guardian.md",
        "Sentinel",
      )
    finally:
      self._spinner.stop()

  # ── Utilities ─────────────────────────────────────────────────

  def _run_agent(
    self, prompt: str, system_file: str, name: str
  ) -> str:
    """Invoke claude --print for one agent; abort on failure."""
    result = subprocess.run(
      [
        "claude", "--print", prompt,
        "--permission-mode", "bypassPermissions",
        "--system-prompt-file",
        str(self._agent_dir / system_file),
      ],
      capture_output=True,
      cwd=str(self._work_dir),
    )
    if result.returncode != 0:
      self._abort(f"Error: {name} failed — aborting.")
    return result.stdout.decode(errors="replace")

  def _require_artifact(self, path: Path) -> None:
    if not path.is_file():
      self._abort(
        f"Error: {path} not found for resume.\n"
        "  Re-run without --from-phase to regenerate."
      )

  @staticmethod
  def _abort(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)
