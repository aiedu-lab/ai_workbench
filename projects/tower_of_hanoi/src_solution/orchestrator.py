"""
orchestrator.py — Orchestrator class.

Wires up Tower, Move, and StepWriter and drives the puzzle from its
initial state to completion.
"""

from __future__ import annotations

from disc import Disc
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
    # Tower 0 starts with all discs; largest at bottom (index 0).
    discs = [Disc(n) for n in range(num_discs, 0, -1)]
    self._towers = [
      Tower(0, num_discs, discs),
      Tower(1, num_discs, []),
      Tower(2, num_discs, []),
    ]
    self._step_writer = StepWriter(
      step_file=step_file, echo_to_stdout=step_by_step
    )
    self._move = Move(
      towers=self._towers,
      num_discs=num_discs,
      step_by_step=step_by_step,
      step_writer=self._step_writer,
    )

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
    while self._move.next():
      pass
    self._step_writer.close()

  def get_towers(self) -> list[Tower]:
    """Return three Tower objects (useful for testing mid-run state)."""
    return self._towers

  def get_move(self) -> Move:
    """Return the Move object (for inspecting step count in tests)."""
    return self._move
