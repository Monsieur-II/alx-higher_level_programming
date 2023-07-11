#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a BaseGeometry class"""

    def area(self):
        """defines the area of shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value of name"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
