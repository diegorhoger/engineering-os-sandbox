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


def power(base, exp):
    if exp < 0:
        return 1 / (base ** abs(exp))
    return base ** exp
