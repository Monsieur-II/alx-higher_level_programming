#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    list_len = len(sys.argv)

    if list_len == 1:
        print("0 arguments.")
    elif list_len == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(list_len - 1))

    if list_len > 1:
        for i in range(1, list_len):
            print("{}: {}".format(i, sys.argv[i]))
