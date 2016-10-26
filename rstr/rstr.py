#!/usr/bin/env python3
"""
Given:
 - a positive integer N
 - a float 1<x>0
 - a string s of upto 10 bp

Return:
The probability that if N random strings having a length of s where constructed
with GC content x, then at least one of the strings equals s. Allowing for the
same string to be created more than once.
"""

from sys import argv


def parse_input(input_file):
    """return [N, x, s]"""
    with open(input_file) as f:
        lines = f.readlines()
    N, x = lines[0].split()
    s = lines[1].strip()
    return [int(N), float(x), str(s)]


def gc_count(s):
    return sum(s.count(i) for i in "GC")


def main(input_list):
    N, x, s = input_list
    gc = gc_count(s)
    at = len(s) - gc
    return 1 - (1-(x/2)**gc * ((1-x)/2)**at)**N


if __name__ == "__main__":
    input_list = parse_input(argv[1])
    ans = main(input_list)
    print("{0:.3f}".format(ans))
