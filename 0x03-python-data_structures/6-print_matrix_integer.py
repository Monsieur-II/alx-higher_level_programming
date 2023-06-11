#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            lin = len(i)
            for j in range(lin):
                print("{:d}".format(i[j]), end="" if j == lin - 1 else " ")
            print()
