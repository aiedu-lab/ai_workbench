"""
orchestrator.py — Orchestrator class.

Wires up Tower, Move, and StepWriter and drives the puzzle from its
initial state to completion.
"""

from __future__ import annotations

from tower import Tower
from move import Move
from step_writer import StepWriter


class Orchestrator:
  """Sets up the puzzle and runs it to completion.

  Responsibilities:
  - Build the three Tower objects with the correct initial state.
  - Instantiate Move and StepWriter with the supplied configuration.
  - Call ``move.next()`` in a loop until the puzzle is solved.

  Args:
    num_discs    (int):  Number of discs (≥ 1).
    step_by_step (bool): Passed through to Move.
    step_file    (str):  Path to the Markdown output
               file; passed to StepWriter.
  """

  def __init__(
    self,
    num_discs: int,
    step_by_step: bool,
    step_file: str,
  ) -> None:
    raise NotImplementedError

  # ------------------------------------------------------------------ #
  # Public interface                                                     #
  # ------------------------------------------------------------------ #

  def run(self) -> None:
    """Execute the puzzle from start to finish.

    Calls ``move.next()`` repeatedly until it returns False, meaning
    Tower[2] holds all discs in the correct order.

    After completion, closes the StepWriter so the output file is
    flushed and finalised.
    """
    raise NotImplementedError

  def get_towers(self) -> list[Tower]:
    """Return three Tower objects (useful for testing mid-run state)."""
    raise NotImplementedError

  def get_move(self) -> Move:
    """Return the Move object (for inspecting step count in tests)."""
    raise NotImplementedError
