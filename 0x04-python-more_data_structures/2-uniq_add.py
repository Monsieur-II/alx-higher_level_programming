#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list
    (once for each integer)"""
    my_set = set(my_list)
    sum = 0

    for i in my_set:
        sum += i
    return sum
