#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Inits a new instance

        Args:
            size (int): size of square
        """
        self.size = size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    @property
    def size(self):
        """Returns: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of size

        Args:
            value (int): value to set as size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns: the area of square"""
        return self.size ** 2
