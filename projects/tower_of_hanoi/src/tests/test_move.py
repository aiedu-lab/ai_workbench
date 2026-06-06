"""
tests/test_move.py — Unit tests for the Move class.
"""

import os
import tempfile

import pytest
from disc import Disc
from tower import Tower
from step_writer import StepWriter
from move import Move


def make_towers(num_discs: int) -> list[Tower]:
  """Return three towers with all discs on Tower[0]."""
  discs = [Disc(n) for n in range(num_discs, 0, -1)]  # largest first
  return [
    Tower(0, num_discs, discs),
    Tower(1, num_discs, []),
    Tower(2, num_discs, []),
  ]


@pytest.fixture
def tmp_step_file(tmp_path):
  return str(tmp_path / "steps.md")


@pytest.fixture
def move_3(tmp_step_file):
  towers = make_towers(3)
  writer = StepWriter(step_file=tmp_step_file, echo_to_stdout=False)
  move = Move(
    towers=towers,
    num_discs=3,
    step_by_step=False,
    step_writer=writer,
  )
  return move, towers, writer


class TestMoveInitialState:
  def test_not_solved_at_start(self, move_3):
    m, towers, _ = move_3
    assert not m.is_solved()


class TestMoveNext:
  def test_next_returns_true_when_moves_remain(self, move_3):
    m, _, _ = move_3
    assert m.next() is True

  def test_next_advances_board_state(self, move_3):
    m, towers, _ = move_3
    m.next()
    # After one move, Tower[0] no longer has all discs
    assert (towers[0].size() < 3
        or towers[1].size() > 0
        or towers[2].size() > 0)

  def test_next_returns_false_when_solved(self, move_3):
    m, _, _ = move_3
    # Exhaust all moves
    while m.next():
      pass
    assert m.next() is False


class TestMoveSolvesCorrectly:
  def test_tower2_has_all_discs_after_completion(self, move_3):
    m, towers, _ = move_3
    while m.next():
      pass
    assert towers[2].as_size_list() == [3, 2, 1]

  def test_tower0_and_tower1_empty_after_completion(self, move_3):
    m, towers, _ = move_3
    while m.next():
      pass
    assert towers[0].is_empty()
    assert towers[1].is_empty()

  def test_total_moves_equals_2n_minus_1(self, tmp_step_file):
    """For N discs the minimum move count must be 2^N - 1."""
    num_discs = 3
    towers = make_towers(num_discs)
    writer = StepWriter(step_file=tmp_step_file, echo_to_stdout=False)
    m = Move(
      towers=towers,
      num_discs=num_discs,
      step_by_step=False,
      step_writer=writer,
    )
    count = 0
    while m.next():
      count += 1
    assert count == 2 ** num_discs - 1


class TestMoveWriteStep:
  def test_write_step_creates_file_content(self, tmp_step_file):
    towers = make_towers(2)
    writer = StepWriter(step_file=tmp_step_file, echo_to_stdout=False)
    m = Move(
      towers=towers,
      num_discs=2,
      step_by_step=False,
      step_writer=writer,
    )
    m.next()
    writer.close()
    content = open(tmp_step_file).read()
    assert "Step" in content
