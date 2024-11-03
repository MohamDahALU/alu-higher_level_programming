#!/usr/bin/python3
"""
This module provides a function to add a new attribute
to an object if possible.
"""


def add_attribute(cls, name, value):
    """
    Adds a new attribute to an object if possible.
    """

    if hasattr(cls, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
