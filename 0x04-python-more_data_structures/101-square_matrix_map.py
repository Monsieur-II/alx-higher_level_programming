#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(list(map(lambda x: x**2, row)), matrix))
