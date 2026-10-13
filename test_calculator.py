"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, square, cube, power


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


def test_square():
    assert square(5) == 25


def test_cube():
    assert cube(3) == 27


def test_power():
    assert power(2, 5) == 32
