#!/usr/bin/python3
"""finding the peak in an array"""


def find_peak(list_of_integers):
    """finding the peak in a list"""
    if list_of_integers == []:
        return None
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    for i in range(1, n - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
           list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
