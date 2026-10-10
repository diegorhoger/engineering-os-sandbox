"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, power


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


def test_power():
    assert power(2, 3) == 8  # 2^3 = 8
    assert power(2, -3) == 0.125  # 2^(-3) = 1/(2^3) = 1/8
    assert power(2, 0) == 1  # 2^0 = 1
    try:
        power(0, -1)  # should raise an error
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        pass
