#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints result

    Returns:
        Value of division, otherwise None
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
