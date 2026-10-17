"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, triple, percent, clamp


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_triple():
    assert triple(4) == 12


def test_percent():
    assert percent(50, 200) == 25.0


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10
