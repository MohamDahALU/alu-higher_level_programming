#!/usr/bin/python3
"""
This module provides a function to add a new attribute
to an object if possible.
"""


def add_attribute(cls, name, value):
    """
    Adds a new attribute to an object if possible.
    """
    try:
        setattr(cls, name, value)
    except Exception:
        raise ValueError("can't add new attribute")
