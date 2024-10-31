#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    A class used to represent a Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Property that retrieves the size of the square (getter).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if value != (int, int) or (value[0], value[1]) < (0, 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints a square made of '#' characters
        with the size defined by the instance attribute __size.
        """
        if self.__size == 0:
            print("")
            return ""
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
