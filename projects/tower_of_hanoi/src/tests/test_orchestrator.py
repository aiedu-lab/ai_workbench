"""
tests/test_orchestrator.py — Unit tests for the Orchestrator class.
"""

import pytest
from orchestrator import Orchestrator
from disc import Disc


@pytest.fixture
def orchestrator(tmp_path):
  return Orchestrator(
    num_discs=3,
    step_by_step=False,
    step_file=str(tmp_path / "steps.md"),
  )


class TestOrchestratorConstruction:
  def test_initial_tower0_has_all_discs(self, orchestrator):
    towers = orchestrator.get_towers()
    assert towers[0].size() == 3

  def test_initial_tower1_is_empty(self, orchestrator):
    towers = orchestrator.get_towers()
    assert towers[1].is_empty()

  def test_initial_tower2_is_empty(self, orchestrator):
    towers = orchestrator.get_towers()
    assert towers[2].is_empty()

  def test_initial_tower0_ordered_correctly(self, orchestrator):
    towers = orchestrator.get_towers()
    assert towers[0].as_size_list() == [3, 2, 1]


class TestOrchestratorRun:
  def test_run_solves_puzzle(self, orchestrator):
    orchestrator.run()
    towers = orchestrator.get_towers()
    assert towers[2].as_size_list() == [3, 2, 1]

  def test_run_empties_tower0(self, orchestrator):
    orchestrator.run()
    assert orchestrator.get_towers()[0].is_empty()

  def test_run_empties_tower1(self, orchestrator):
    orchestrator.run()
    assert orchestrator.get_towers()[1].is_empty()

  def test_run_writes_step_file(self, tmp_path):
    step_file = str(tmp_path / "steps.md")
    orch = Orchestrator(
      num_discs=3,
      step_by_step=False,
      step_file=step_file,
    )
    orch.run()
    import os
    assert os.path.exists(step_file)
    assert os.path.getsize(step_file) > 0

  def test_run_correct_move_count(self, tmp_path):
    """2^N - 1 moves for N discs."""
    num_discs = 4
    orch = Orchestrator(
      num_discs=num_discs,
      step_by_step=False,
      step_file=str(tmp_path / "s.md"),
    )
    orch.run()
    step_file_content = open(str(tmp_path / "s.md")).read()
    # Count "## Step" headings as a proxy for move count
    move_count = step_file_content.count("## Step")
    assert move_count == 2 ** num_discs - 1
