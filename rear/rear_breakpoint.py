#!/usr/bin/env python3
# NOTE: not working
from sys import argv
from rear import read_input, reversal


def find_breakpoints(seq):
    """ return indices of breakpoints """
    breakpoints = []
    for i in range(len(seq)-1):
        if seq[i] - seq[i+1] != -1:
            breakpoints.append((i, i+1))
    return breakpoints


# def grouped_iter(iterable, n):
#     """ loop through list two elements at a time """
#     return zip(*[iter(iterable)]*n)


if __name__ == "__main__":
    test = [1, 4, 3, 2, 5]
    breaks = find_breakpoints(test)
    print(test)
    print(breaks)
