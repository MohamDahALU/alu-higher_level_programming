#!/usr/bin/python3
"""
This module defines a Base class that serves as the foundation
for other classes in the project.
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

        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
