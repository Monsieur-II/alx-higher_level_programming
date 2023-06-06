#!/usr/bin/python3

for i in range(9):
    if i == 8:
        print("{:d}".format(89))
    else:
        for j in range(i + 1, 10):
            print("{:d}{:d}".format(i, j), end=", ")
