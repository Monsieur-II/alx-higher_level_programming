#!/usr/bin/python3
"""Defines an integer addition fucntion"""


def add_integer(a, b=98):
    """Returns the integer sum of a and b

    Argument b is optional but all arguments must be ints or floats

    Raises:
        TyepError: if either of arguments is not an int or a float
    """
    if not(isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not(isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
