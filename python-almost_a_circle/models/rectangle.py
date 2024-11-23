#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from the Base class.
"""


class Base:
    """
    Base class for managing id attribute in all future
    classes and to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        """

        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = self.__nb_objects


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the private attribute __x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the Rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the private attribute __y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y-coordinate of the Rectangle.
        """
        self.__y = value
