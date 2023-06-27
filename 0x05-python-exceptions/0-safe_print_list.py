#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list

    Returns:
        Number of elements printed
    """
    res = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            res += 1
        except IndexError:
            print()
            return res

    print()
    return res
