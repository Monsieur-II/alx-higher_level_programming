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

    def area(self):
        """Returns the area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
