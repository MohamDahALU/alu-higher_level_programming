#!/usr/bin/python3
"""
This module defines the Square class, which inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance with size,
        x and y coordinates, and an optional id.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square, which is equivalent to its width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square by updating both width and height.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
