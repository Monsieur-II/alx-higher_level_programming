#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts Roman numeral to integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        if i not in list(r_dict):
            return (0)
    sum = 0
    i = 0
    while i < len(roman_string):
        y = i + 1
        current = roman_string[i]
        if i == (len(roman_string) - 1):
            sum += r_dict[current]
            break
        next = roman_string[y]
        if r_dict[current] < r_dict[next]:
            sum -= r_dict[current]
        else:
            sum += r_dict[current]
        i += 1
    return (sum)
