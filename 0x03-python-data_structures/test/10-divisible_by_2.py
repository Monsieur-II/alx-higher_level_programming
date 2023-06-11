#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for i in my_list:
            if i == 0:
                new_list.append(True)
            elif i % 2:
                new_list.append(False)
            else:
                new_list.append(True)

        return new_list
