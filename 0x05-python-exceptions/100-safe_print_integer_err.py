#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer"""
    try:
        print("{:d}".format(value))
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    else:
        return True
