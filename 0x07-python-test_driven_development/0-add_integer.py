#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Returns the sum of a and b

    Argument b is optional but all arguments must be ints or floats

    Raises:
        TypeError: if either of the args is not an int or a float
    """
    if not(isinstance(a, int)) and not(isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not(isinstance(b, int)) and not(isinstance(b, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
