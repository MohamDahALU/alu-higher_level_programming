#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """

    try:
        float(a)
    except Exception:
        raise TypeError("a must be an integer")
    try:
        float(b)
    except Exception:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b