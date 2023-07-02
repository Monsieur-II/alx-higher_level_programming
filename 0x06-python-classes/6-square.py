#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Inits a new instance

        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(axis, int) for axis in value) and
                all(axis >= 0 for axis in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns: the area of square"""
        return self.size ** 2

    def my_print(self):
        """Prints square with '#'"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            x = self.position[0]
            for i in range(self.__size):
                print(' ' * x, end="")
                print('#' * self.__size)
