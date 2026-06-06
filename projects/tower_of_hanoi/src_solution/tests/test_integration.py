"""
tests/test_integration.py — End-to-end integration tests.

These tests treat the system as a black box: construct an Orchestrator,
run it, and verify externally observable outcomes only.
"""

import os
import pytest
from orchestrator import Orchestrator


def run_puzzle(tmp_path, num_discs: int) -> tuple:
  """Helper: run the puzzle and return (orchestrator, step_file_path)."""
  step_file = str(tmp_path / f"steps_{num_discs}.md")
  orch = Orchestrator(
    num_discs=num_discs,
    step_by_step=False,
    step_file=step_file,
  )
  orch.run()
  return orch, step_file


class TestEndToEndSmall:
  @pytest.mark.parametrize("num_discs", [1, 2, 3])
  def test_puzzle_solved_for_n_discs(self, tmp_path, num_discs):
    """Tower[2] holds all discs in order for 1–3 disc configurations."""
    orch, _ = run_puzzle(tmp_path, num_discs)
    towers = orch.get_towers()
    expected = list(range(num_discs, 0, -1))
    assert towers[2].as_size_list() == expected

  @pytest.mark.parametrize("num_discs", [1, 2, 3])
  def test_correct_move_count(self, tmp_path, num_discs):
    """Step file records exactly 2^N − 1 moves for N discs."""
    _, step_file = run_puzzle(tmp_path, num_discs)
    content = open(step_file).read()
    move_count = content.count("## Step")
    assert move_count == 2 ** num_discs - 1

  @pytest.mark.parametrize("num_discs", [1, 2, 3])
  def test_step_file_exists_and_nonempty(self, tmp_path, num_discs):
    """The step file exists and contains content after run completes."""
    _, step_file = run_puzzle(tmp_path, num_discs)
    assert os.path.exists(step_file)
    assert os.path.getsize(step_file) > 0


class TestEndToEndLarger:
  def test_puzzle_solved_for_5_discs(self, tmp_path):
    """Solver scales to 5 discs; all towers end in expected state."""
    orch, _ = run_puzzle(tmp_path, 5)
    towers = orch.get_towers()
    assert towers[2].as_size_list() == [5, 4, 3, 2, 1]
    assert towers[0].is_empty()
    assert towers[1].is_empty()

  def test_no_disc_ordering_violation_throughout(self, tmp_path):
    """After every move, each tower must have discs in descending order."""
    from disc import Disc
    from tower import Tower
    from move import Move
    from step_writer import StepWriter

    num_discs = 4
    discs = [Disc(n) for n in range(num_discs, 0, -1)]
    towers = [
      Tower(0, num_discs, discs),
      Tower(1, num_discs, []),
      Tower(2, num_discs, []),
    ]
    step_file = str(tmp_path / "integrity.md")
    writer = StepWriter(step_file=step_file, echo_to_stdout=False)
    move = Move(
      towers=towers,
      num_discs=num_discs,
      step_by_step=False,
      step_writer=writer,
    )

    while move.next():
      for t in towers:
        sizes = t.as_size_list()
        # Each tower must be strictly descending (largest at bottom)
        assert sizes == sorted(sizes, reverse=True), (
          f"Tower ordering violated: {sizes}"
        )
