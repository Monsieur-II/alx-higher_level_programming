#!/usr/bin/python3
"""Defines a file reading function"""


def read_file(filename=""):
    """reads a text file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
