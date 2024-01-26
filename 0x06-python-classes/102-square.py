#!/usr/bin/python3
"""This defines the class 'Square'."""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """Initialize the square.
        Args:
            size (int): Size of the square."""
        self.size = size

    @property
    def size(self):
        """This gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines the operator == to the Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the operator != to the Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the operator < to the Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the operator <= to the Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the operator > to the Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """This defines the operator >= to the Square."""
        return self.area() >= other.area()
