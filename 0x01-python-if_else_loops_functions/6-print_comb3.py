#!/usr/bin/python3

for i in range(9):
    if i == 8:
        print(f"{89:d}")
    else:
        for j in range(i + 1, 10):
            print(f"{i:d}{j:d}", end=", ")
