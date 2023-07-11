#!/usr/bin/python3
""" Defines a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square"""

    def __init__(self, size):
        """Inits an instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (size ** 2)
