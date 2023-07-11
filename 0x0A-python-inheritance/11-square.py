#!/usr/bin/python3
""" Defines a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square"""

    def __init__(self, size):
        """Inits an instance"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """String representation of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)
