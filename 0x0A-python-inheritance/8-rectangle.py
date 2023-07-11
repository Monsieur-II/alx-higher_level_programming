#!/usr/bin/python3
"""Defines a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reps a rectangle"""
    def __init__(self, width, height):
        """Inits an instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
