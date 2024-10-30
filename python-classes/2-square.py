#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    size : int
        The size of the square's side.
    """

    def __init__(self, size=0):
        """
        Initialize the square, and validate.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
