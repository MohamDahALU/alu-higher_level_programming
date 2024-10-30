#!/usr/bin/python3


"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
