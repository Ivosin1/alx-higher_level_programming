#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""

import math


class MagicClass:
    """This represents a circle."""

    def __init__(self, radius=0):
        """This initializes a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """This returns the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
