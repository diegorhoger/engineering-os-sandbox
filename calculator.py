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


def triple(x):
    return x * 3


def percent(part, total):
    return (part / total) * 100


def clamp(x, lo, hi):
    return max(lo, min(x, hi))
