#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists

    Returns a new list
    """
    new = list()
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            res = 0
            print("out of range")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        finally:
            new.append(res)
    return new
