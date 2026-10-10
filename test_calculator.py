"""Tests for calculator module."""

from calculator import add, subtract, multiply, divide, modulo, factorial, gcd


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


def test_modulo():
    assert modulo(5, 3) == 2
    assert modulo(10, 2) == 0
    assert modulo(-9, 4) == 3
    assert modulo(7, -3) == -2


def test_modulo_by_zero():
    try:
        modulo(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative():
    try:
        factorial(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_gcd():
    assert gcd(12, 8) == 4
    assert gcd(17, 5) == 1
    assert gcd(100, 10) == 10
    assert gcd(-12, 8) == 4
    assert gcd(0, 5) == 5
