"""orchestrator.py — Piper: book-to-mindmap pipeline orchestrator.

Sequences the five pipeline phases (sanitizer → setup →
converter → Seth → validator-loop) and implements the
coordination doctrine from agents/piper-pipeline-orchestrator.md:
task scope locking, agent sequencing, retry policy (up to 3),
and independent final verification via Sentinel.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

from display import PhaseDisplay
from spinner import Spinner

# Maps phase name → (main_phase_idx, vl_sub_idx).
# vl_sub_idx: 0=start from Leo, 1=skip Leo (quinn resume),
#             2=skip Leo+Quinn (sentinel resume).
_PHASE_MAP: dict[str, tuple[int, int]] = {
  "sanitizer":      (0, 0),
  "setup":          (1, 0),
  "converter":      (2, 0),
  "seth":           (3, 0),
  "validator-loop": (4, 0),
  "leo":            (4, 0),
  "quinn":          (4, 1),
  "sentinel":       (4, 2),
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
    log_dir: str | None = None,
    waterfall_log: str | None = None,
  ) -> None:
    main_idx, vl_start = _PHASE_MAP[from_phase]
    self._input = input_path
    self._from_idx = main_idx
    self._vl_start = vl_start
    self._log_dir: Path | None = (
      Path(log_dir).resolve() if log_dir else None
    )
    if self._log_dir:
      self._log_dir.mkdir(parents=True, exist_ok=True)
    self._script_dir = Path(__file__).resolve().parent.parent
    self._agent_dir = self._script_dir / "agents"
    self._display = PhaseDisplay(
      log_path=waterfall_log,
    )
    self._display.vl_max = self.MAX_RETRIES
    self._spinner = Spinner()
    # Resolved during sanitizer phase
    self._book_name: str = ""
    self._ext: str = ""
    self._is_url: bool = False
    self._abs_input: str = ""
    self._abs_output = Path(output_path)
    self._output_dir: Path = Path()
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
    self._update_read_list("done")
    return 0

  # ── Phase: Argument Sanitizer ─────────────────────────────────

  def _phase_sanitizer(self) -> None:
    inp = self._input
    self._is_url = inp.startswith(("http://", "https://"))
    if self._is_url:
      # Extract extension from URL path; default html for
      # extensionless web pages (e.g. /blog/article-title).
      from urllib.parse import urlparse
      path = urlparse(inp).path
      ext = (
        path.rsplit(".", 1)[-1].lower()
        if "." in path else ""
      )
      if ext not in _VALID_EXT:
        ext = "html"
    else:
      ext = inp.rsplit(".", 1)[-1].lower() if "." in inp else ""
      if ext not in _VALID_EXT:
        self._abort(
          f"Error: unsupported extension '.{ext}'.\n"
          f"  Supported: {' '.join(sorted(_VALID_EXT))}"
        )
    self._ext = ext
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
    self._book_name = book_name
    out = self._abs_output
    out.parent.mkdir(parents=True, exist_ok=True)
    self._abs_output = out.parent.resolve() / out.name
    output_dir = self._abs_output.parent
    self._output_dir = output_dir
    self._work_dir = output_dir / ".tmp"
    self._notes_file = (
      self._work_dir / f"{book_name}-detailed-notes.md"
    )
    self._content_json = (
      self._work_dir / f"{book_name}-mindmap-content.json"
    )
    # Placeholder — overridden per attempt in _phase_validator_loop
    # to .tmp/<book>-mindmap-{N}.html so each attempt is versioned.
    # run() copies the approved attempt to output_dir.
    self._html_file = (
      self._work_dir / f"{book_name}-mindmap.html"
    )
    # Delete stale book logs before any agent starts so
    # watchers (tail -f) see a clean break between runs.
    if self._log_dir:
      for stale in self._log_dir.glob(f"{book_name}-*.log"):
        stale.unlink(missing_ok=True)

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
    self._update_read_list("converter")

  def _convert_input(self) -> None:
    ext, inp = self._ext, self._abs_input
    notes = str(self._notes_file)
    if ext == "pdf":
      subprocess.run(["pdftotext", inp, notes], check=True)
    elif ext in ("html", "htm") and self._is_url:
      # Download to contents/ subfolder for corpus archival.
      # Keeps raw source separate from generated mindmap output.
      contents = self._output_dir / "contents"
      contents.mkdir(exist_ok=True)
      local = contents / f"{self._book_name}.html"
      curl = subprocess.run(
        ["curl", "-fsSL", inp],
        capture_output=True, check=True,
      )
      local.write_bytes(curl.stdout)
      out = subprocess.run(
        ["html2text", str(local)],
        capture_output=True, check=True,
      )
      self._notes_file.write_bytes(out.stdout)
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
      self._validate_json(self._content_json)
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
    self._validate_json(self._content_json)
    self._display.ph[3] = "done"
    self._update_read_list("seth")

  # ── Phase: Validator Loop (Leo → Quinn → Sentinel) ────────────

  def _phase_validator_loop(self) -> None:
    self._display.ph[4] = "active"
    for attempt in range(1, self.MAX_RETRIES + 1):
      # Version HTML by attempt so the draft history is preserved.
      # run() copies the approved file to output_dir after success.
      self._html_file = (
        self._work_dir
        / f"{self._book_name}-mindmap-{attempt}.html"
      )
      self._display.vl_attempt = attempt
      skip_leo = (attempt == 1 and self._vl_start > 0)
      skip_quinn = (attempt == 1 and self._vl_start > 1)
      # When resuming, the attempt-1 HTML must already exist.
      if attempt == 1 and self._vl_start > 0:
        self._require_artifact(self._html_file)
        self._validate_html(self._html_file)
      if self._validator_attempt(attempt, skip_leo, skip_quinn):
        self._display.ph[4] = "done"
        return
    self._abort("Error: max retries reached.")

  def _validator_attempt(
    self,
    attempt: int,
    skip_leo: bool = False,
    skip_quinn: bool = False,
  ) -> bool:
    """Run one Leo→Quinn→Sentinel cycle. True if approved."""
    if skip_leo:
      self._display.vl = ["done", "active", "pending"]
      self._display.waterfall()
    else:
      self._display.vl = ["active", "pending", "pending"]
      self._display.waterfall()
      try:
        self._run_leo(attempt)
      except SystemExit:
        pass  # file-validity check below handles retry/abort
      html_ok = self._html_file.is_file() and self._is_html_ok(
        self._html_file
      )
      if not html_ok:
        # Remove partial file so resume via --from-phase leo
        # doesn't silently accept incomplete output.
        self._html_file.unlink(missing_ok=True)
        self._display.vl = ["skip", "skip", "skip"]
        if attempt >= self.MAX_RETRIES:
          self._display.ph[4] = "active"
          self._display.waterfall()
          self._abort(
            f"Error: Leo did not produce valid HTML"
            f" in {self._html_file} — max retries."
          )
        self._display.waterfall()
        return False
      self._display.vl = ["done", "active", "pending"]
      self._display.waterfall()
    if not skip_quinn:
      quinn_out = self._run_quinn(attempt)
      if not quinn_out.strip() or "NOT APPROVED" in quinn_out:
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
    sent_out = self._run_sentinel(attempt)
    if not sent_out.strip() or "NOT APPROVED" in sent_out:
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

  def _run_leo(self, attempt: int) -> None:
    self._spinner.start(
      "Leo · rendering vis-network mindmap HTML..."
    )
    try:
      self._run_agent(
        f"Render {self._content_json} into {self._html_file}",
        "leo-layout-engineer.md",
        "Leo",
        attempt=attempt,
      )
    finally:
      self._spinner.stop()

  def _run_quinn(self, attempt: int) -> str:
    self._spinner.start(
      "Quinn · reviewing layout, hierarchy, content..."
    )
    try:
      return self._run_agent(
        f"Review {self._html_file} for quality issues.",
        "quinn-qa-reviewer.md",
        "Quinn",
        attempt=attempt,
      )
    finally:
      self._spinner.stop()

  def _run_sentinel(self, attempt: int) -> str:
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
        attempt=attempt,
      )
    finally:
      self._spinner.stop()

  # ── Utilities ─────────────────────────────────────────────────

  def _run_agent(
    self,
    prompt: str,
    system_file: str,
    name: str,
    attempt: int | None = None,
  ) -> str:
    """Invoke claude --print; stream stdout to log if --log-dir set.

    Uses --output-format stream-json for real-time line emission.
    Extracts text from assistant events; checks result.subtype for
    success. Log: {book}-{agent}[-{attempt}].log — tail to track
    progress. Waterfall and spinner are unaffected.
    """
    cmd = [
      "claude", "--print", "--verbose", prompt,
      "--output-format", "stream-json",
      "--permission-mode", "bypassPermissions",
      "--system-prompt-file",
      str(self._agent_dir / system_file),
    ]
    suffix = f"-{attempt}" if attempt is not None else ""
    log_path = (
      self._log_dir
      / f"{self._book_name}-{name.lower()}{suffix}.log"
      if self._log_dir else None
    )
    parts: list[str] = []
    failed = False
    result_seen = False
    lf = log_path.open("w", encoding="utf-8") if log_path else None
    # DEBUG: raw event log to diagnose stream-json format.
    # Written alongside the text log; remove once format confirmed.
    raw_log_path = (
      log_path.with_suffix(".raw.jsonl") if log_path else None
    )
    rlf = (
      raw_log_path.open("w", encoding="utf-8")
      if raw_log_path else None
    )
    try:
      with subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        cwd=str(self._work_dir),
      ) as proc:
        for raw in proc.stdout:
          if rlf:
            rlf.write(raw.decode("utf-8", errors="replace"))
            rlf.flush()
          try:
            evt = json.loads(raw)
          except json.JSONDecodeError:
            continue
          if evt.get("type") == "assistant":
            for blk in evt.get("message", {}).get("content", []):
              if blk.get("type") == "text":
                text = blk["text"]
                parts.append(text)
                if lf:
                  lf.write(text)
                  lf.flush()
          elif evt.get("type") == "result":
            result_seen = True
            if evt.get("subtype") != "success":
              failed = True
    finally:
      if lf:
        lf.close()
      if rlf:
        rlf.close()
    if failed or not result_seen:
      self._abort(f"Error: {name} failed — aborting.")
    return "".join(parts)

  def _update_read_list(self, phase: str) -> None:
    """Upsert a status line in read-list.md for this book.

    Status symbols:
      [ ]        — not yet started
      [<phase>]  — last completed phase (converter/seth/leo/quinn)
      [✓]        — mindmap fully built and saved
    Finds the existing line by book_name and updates in place,
    or appends a new entry if none exists.
    """
    rl = self._output_dir / "read-list.md"
    status = "[✓]" if phase == "done" else f"[{phase}]"
    mindmap_name = self._abs_output.name
    entry = (
      f"- {status} [{self._book_name}]({mindmap_name})"
      f" — `{self._abs_input}`\n"
    )
    header = (
      "# Speed Reading — Processed Materials\n\n"
      "<!-- Status: [ ] not started"
      " · [<phase>] last phase done"
      " · [✓] mindmap complete -->\n\n"
    )
    if rl.exists():
      lines = rl.read_text(encoding="utf-8").splitlines(
        keepends=True
      )
      for i, line in enumerate(lines):
        if f"[{self._book_name}]" in line:
          lines[i] = entry
          rl.write_text("".join(lines), encoding="utf-8")
          return
      with rl.open("a", encoding="utf-8") as f:
        f.write(entry)
    else:
      rl.write_text(header + entry, encoding="utf-8")

  def _require_artifact(self, path: Path) -> None:
    if not path.is_file() or path.stat().st_size == 0:
      self._abort(
        f"Error: {path} missing or empty for resume.\n"
        "  Re-run without --from-phase to regenerate."
      )

  def _validate_json(self, path: Path) -> None:
    try:
      json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
      self._abort(
        f"Error: {path} contains invalid JSON.\n"
        "  Re-run from the seth phase to regenerate."
      )

  def _validate_html(self, path: Path) -> None:
    if not self._is_html_ok(path):
      self._abort(
        f"Error: {path} is incomplete (missing </html>).\n"
        "  Re-run with --from-phase leo to regenerate."
      )

  @staticmethod
  def _is_html_ok(path: Path) -> bool:
    """Return True only if file ends with a closing html tag."""
    try:
      text = path.read_text(encoding="utf-8", errors="replace")
      return "</html>" in text.lower()
    except OSError:
      return False

  @staticmethod
  def _abort(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)
