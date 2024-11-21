#!/usr/bin/python3
"""
This module provides a function to print a square
"""


def text_indentation(text):
    """
    prints each segment separated by two newlines.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = text.replace("? ", ". ")
    new_str = new_str.replace(": ", ". ")
    new_str = text.split(". ")
    print("\n\n".join(new_str), end="")
