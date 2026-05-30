"""spinner.py — Spinner: animated stderr spinner during agent calls.

Runs in a daemon thread so the main thread stays unblocked
while a claude subprocess is running.
"""
import sys
import threading
import time


class Spinner:
  """Animated stderr spinner during active agent calls."""

  _CHARS = r"/-\|"

  def __init__(self) -> None:
    self._thread: threading.Thread | None = None
    self._stop = threading.Event()

  def start(self, label: str) -> None:
    """Start spinner with given label text on stderr."""
    self._stop.clear()

    def _spin() -> None:
      i = 0
      while not self._stop.is_set():
        print(
          f"  [{self._CHARS[i % 4]}] {label}\r",
          end="", file=sys.stderr,
        )
        time.sleep(0.15)
        i += 1

    self._thread = threading.Thread(target=_spin, daemon=True)
    self._thread.start()

  def stop(self) -> None:
    """Stop spinner and erase the spinner line."""
    if self._thread is not None:
      self._stop.set()
      self._thread.join()
      self._thread = None
      print(" " * 70 + "\r", end="", file=sys.stderr)
