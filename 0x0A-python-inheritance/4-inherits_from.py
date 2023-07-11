#!/usr/bin/python3
"""Defines a function that checks for subclasses"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited directly or indirectly from the specified class
    """
    return (issubclass(obj, a_class))
