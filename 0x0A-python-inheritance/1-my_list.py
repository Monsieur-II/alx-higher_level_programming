#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Implements a class that inherits from list"""

    def __init__(self):
        """Inits an instance"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
