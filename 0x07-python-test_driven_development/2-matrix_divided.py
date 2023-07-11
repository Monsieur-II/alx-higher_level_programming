#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): the matrix to divide
        div (): the divisor, must not be zero (0)

    Returns: a new matrix
    """
    if (not matrix or not isinstance(matrix, list) or
       (any((not row or not isinstance(row, list)) for row in matrix))):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if any(not isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = list(list(map(lambda x: round(x / div, 2), row))
                    for row in matrix)

    return (new_list)
