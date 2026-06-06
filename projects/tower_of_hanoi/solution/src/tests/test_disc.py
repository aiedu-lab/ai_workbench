"""
tests/test_disc.py — Unit tests for the Disc class.
"""

import pytest
from disc import Disc


class TestDiscConstruction:
  def test_valid_disc_size(self):
    """A Disc created with a positive size should store that size."""
    disc = Disc(3)
    assert disc.size == 3

  def test_size_one_is_valid(self):
    """The minimum valid disc size (1) is accepted without error."""
    disc = Disc(1)
    assert disc.size == 1

  def test_zero_size_raises(self):
    """Size 0 raises ValueError — discs must be positive integers."""
    with pytest.raises(ValueError):
      Disc(0)

  def test_negative_size_raises(self):
    """Negative sizes raise ValueError."""
    with pytest.raises(ValueError):
      Disc(-1)


class TestDiscComparisons:
  def test_equal_discs(self):
    """Two Disc objects with the same size compare equal."""
    assert Disc(2) == Disc(2)

  def test_smaller_disc_less_than_larger(self):
    """The < operator respects disc size ordering."""
    assert Disc(1) < Disc(3)

  def test_larger_disc_not_less_than_smaller(self):
    """A larger disc is not less than a smaller one."""
    assert not (Disc(3) < Disc(1))

  def test_discs_of_different_sizes_not_equal(self):
    """Discs with different sizes are not equal."""
    assert Disc(1) != Disc(2)


class TestDiscRepr:
  def test_repr_contains_size(self):
    """repr() includes the size value for readable debug output."""
    assert "2" in repr(Disc(2))
