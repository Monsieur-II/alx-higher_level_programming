#!/usr/bin/python3

"""Writes a class Square that defines a square
    by size"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initialises a new instance

        Args:
            size (int): size of square
        """
        self.__size = size
