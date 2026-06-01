"""
step_writer.py — PROVIDED UTILITY.  Students do not need to modify this file.

Writes each puzzle step as a Markdown section to a file, and optionally
echoes the same content to stdout.

Usage:
    writer = StepWriter(step_file="./solution.md", echo_to_stdout=False)
    writer.write(
        step_number=1,
        from_tower=0,
        to_tower=2,
        ascii_art="...",   # string returned by AsciiRenderer.render()
    )
    writer.close()
"""

from __future__ import annotations

import io


class StepWriter:
    """Writes step-by-step puzzle state to a Markdown file.

    Each call to ``write()`` appends one section to the file.  The file
    is kept open between calls for efficiency; call ``close()`` when
    the puzzle is finished.

    Args:
        step_file      (str):  Path to the output Markdown file.
                               Created (or overwritten) on construction.
        echo_to_stdout (bool): If True each step is also printed to stdout.
    """

    def __init__(self, step_file: str, echo_to_stdout: bool = False) -> None:
        self._path = step_file
        self._echo = echo_to_stdout
        self._fh: io.TextIOWrapper = open(step_file, "w", encoding="utf-8")
        self._fh.write("# Tower of Hanoi — Solution Steps\n\n")

    # ------------------------------------------------------------------ #
    # Public                                                               #
    # ------------------------------------------------------------------ #

    def write(
        self,
        step_number: int,
        from_tower: int,
        to_tower: int,
        ascii_art: str,
    ) -> None:
        """Append one step to the file (and optionally stdout).

        Args:
            step_number: 1-based counter.
            from_tower:  Source tower index.
            to_tower:    Destination tower index.
            ascii_art:   Pre-rendered string from AsciiRenderer.render().
        """
        heading = f"## Step {step_number}: Move disc from Tower[{from_tower}] → Tower[{to_tower}]\n\n"
        block = f"```\n{ascii_art}\n```\n\n"
        section = heading + block

        self._fh.write(section)
        self._fh.flush()

        if self._echo:
            print(section, end="")

    def write_initial(self, ascii_art: str) -> None:
        """Write the initial board state before any moves are made."""
        heading = "## Initial State\n\n"
        block = f"```\n{ascii_art}\n```\n\n"
        section = heading + block
        self._fh.write(section)
        self._fh.flush()
        if self._echo:
            print(section, end="")

    def close(self) -> None:
        """Flush and close the output file."""
        if not self._fh.closed:
            self._fh.write("---\n*Puzzle solved!*\n")
            self._fh.close()

    def __enter__(self) -> "StepWriter":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
