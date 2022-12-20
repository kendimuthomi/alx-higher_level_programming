#!/usr/bin/python3
"""finding the peak in an array"""


def find_peak(list_of_integers):
    """finding the peak in a list"""
    if list_of_integers == []:
        return None
    n = len(list_of_integers)
    mid = n / 2
    mid = int(mid)
    ele = list_of_integers[mid]
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    if ele > list_of_integers[mid - 1] and ele > list_of_integers[mid + 1]:
        return ele
    elif ele < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
