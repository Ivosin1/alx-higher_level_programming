#!/usr/bin/python3
"""This defines a class 'Square'."""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """This initializes the square.
        Args:
            size (int): Size of the square."""
        self.size = size

    @property
    def size(self):
        """It gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Should return the area of the square."""
        return (self.__size * self.__size)
