"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, negate, double


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


def test_negate():
    assert negate(5) == -5


def test_double():
    assert double(4) == 8
