#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo  # midpoint
    mid = int(mid)

    # if list has only one member return the number
    if hi == 1:
        return list_of_integers[0]

    # if list has two members return the larger one
    if hi == 2:
        return max(list_of_integers)

    # this algorithim starts searching for peak from the middle
    if list_of_integers[mid - 1] <= list_of_integers[mid] >= \
            list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
