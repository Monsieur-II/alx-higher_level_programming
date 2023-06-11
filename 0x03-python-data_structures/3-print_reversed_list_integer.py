#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reversed order"""
    if my_list:
        new_list = my_list.copy()
        new_list.reverse()
        for i in new_list:
            print("{:d}".format(i))
