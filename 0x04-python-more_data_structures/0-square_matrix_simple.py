#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes square value of all integers"""
    new = list(list(map(lambda x: x**2, row)) for row in matrix)
    return (new)
