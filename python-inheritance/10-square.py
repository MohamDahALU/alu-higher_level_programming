#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, which
    inherits from BaseGeometry.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size


s = Square(13)

print(s)
print(s.area())
