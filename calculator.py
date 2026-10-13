"""Simple calculator module for end-to-end testing."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def negate(x):
    return -x


def double(x):
    return add(x, x)


def abs_diff(a, b):
    diff = a - b
    if diff < 0:
        return negate(diff)
    return diff
