#!/usr/bin/env python3

# NOTE: not working

from sys import argv
import copy

"""
Given a collection of 5 pairs of permutations, all of which have a length of 10
Return the reversal distance between each perumutation pair

e.g

1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

9
"""


def read_input(in_file):
    """parse input into a list of tuples"""
    # get lists of integers
    out = []
    with open(in_file) as f:
        for line in f:
            nums = [int(i) for i in line.split()]
            if len(nums) > 0:
                out.append(nums)
    assert len(out) & len(nums) == 10
    # create tuples from pairs of lines
    return [(out[i], out[i+1]) for i in range(0, len(out), 2)]


def reversal(x, start, stop):
    x[start:stop+1] = reversed(x[start:stop+1])


def flip(x, n):
    loc_n = x.index(n)
    new_seq = reversal(x, n-1, loc_n)
    return new_seq


def naive(x):
    """ sort x by reversals, return number of reversals """
    for i in range(1, len(x)):
        print(x)
        flip(x, i)
        if sorted(x) == x:
            return i


if __name__ == "__main__":
    test = [5, 2, 4, 1, 3]
    output = naive(test)
    print(output)

