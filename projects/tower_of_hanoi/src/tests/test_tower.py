"""
tests/test_tower.py — Unit tests for the Tower class.
"""

import pytest
from disc import Disc
from tower import Tower


@pytest.fixture
def empty_tower() -> Tower:
    return Tower(index=0, num_discs=3, discs=[])


@pytest.fixture
def full_tower() -> Tower:
    """Tower 0 loaded with 3 discs (largest at bottom)."""
    return Tower(index=0, num_discs=3, discs=[Disc(3), Disc(2), Disc(1)])


class TestTowerConstruction:
    def test_empty_tower_is_empty(self, empty_tower):
        assert empty_tower.is_empty()

    def test_full_tower_not_empty(self, full_tower):
        assert not full_tower.is_empty()

    def test_full_tower_correct_size(self, full_tower):
        assert full_tower.size() == 3


class TestTowerPeek:
    def test_peek_returns_top_disc(self, full_tower):
        assert full_tower.peek() == Disc(1)

    def test_peek_on_empty_returns_none(self, empty_tower):
        assert empty_tower.peek() is None

    def test_peek_does_not_remove_disc(self, full_tower):
        full_tower.peek()
        assert full_tower.size() == 3


class TestTowerPop:
    def test_pop_returns_top_disc(self, full_tower):
        assert full_tower.pop() == Disc(1)

    def test_pop_decrements_size(self, full_tower):
        full_tower.pop()
        assert full_tower.size() == 2

    def test_pop_empty_tower_raises(self, empty_tower):
        with pytest.raises(IndexError):
            empty_tower.pop()


class TestTowerPush:
    def test_push_increases_size(self, empty_tower):
        empty_tower.push(Disc(2))
        assert empty_tower.size() == 1

    def test_push_smaller_disc_on_larger_is_valid(self, empty_tower):
        empty_tower.push(Disc(3))
        empty_tower.push(Disc(1))   # smaller on top → legal
        assert empty_tower.peek() == Disc(1)

    def test_push_larger_disc_on_smaller_raises(self, empty_tower):
        empty_tower.push(Disc(1))
        with pytest.raises(ValueError):
            empty_tower.push(Disc(3))   # larger on smaller → illegal


class TestTowerAsSizeList:
    def test_full_tower_size_list(self, full_tower):
        assert full_tower.as_size_list() == [3, 2, 1]

    def test_empty_tower_size_list(self, empty_tower):
        assert empty_tower.as_size_list() == []


class TestTowerDisplay:
    def test_display_does_not_raise(self, full_tower, capsys):
        """display() should print something without raising."""
        full_tower.display()
        captured = capsys.readouterr()
        assert len(captured.out) > 0
