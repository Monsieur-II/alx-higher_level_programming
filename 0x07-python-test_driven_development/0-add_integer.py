#!/usr/bin/python3
"""Defines an integer addition fucntion"""


def add_integer(a, b=98):
    """Performs addition operation on two arguments

    Args:
            a (int, float): First operand
            b (int, float): Second operand (optional)

    Returns:
             the sum of a and b
    """
    if not(isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not(isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
