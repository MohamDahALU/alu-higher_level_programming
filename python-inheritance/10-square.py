#!/usr/bin/python3
"""
This module defines a BaseGeometry class.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class used to represent a Rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(width, height)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


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
