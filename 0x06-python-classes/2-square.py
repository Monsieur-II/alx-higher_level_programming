#!/usr/bin/python3

"""Defines a square by size"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Inits a new instance

        Args:
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
