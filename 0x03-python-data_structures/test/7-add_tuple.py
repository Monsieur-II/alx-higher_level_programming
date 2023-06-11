#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple with 2 elements:
    First element is the sum of first elements in tuple a and b
    Second is the sum of second elements in tuple a and b"""

    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)

    '''The lines above concatenates tuple a and b each with the tuple (0, 0)
    and assignes the result to new variables which we will work with.
    This caters for scenarios where tuples a and b have less than 2 elements'''

    new_tuple = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return new_tuple
