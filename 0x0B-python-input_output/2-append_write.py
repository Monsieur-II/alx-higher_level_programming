#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text fil

    Returns: number of chars read
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
