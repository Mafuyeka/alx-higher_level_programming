#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    list_len = len(list_of_integers)
    if list_len == 1:
        return list_of_integers[0]
    mid = list_len // 2
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    elif mid < list_len - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return list_of_integers[mid]


# Complexity: O(log(n))
