#!/usr/bin/env python3

"""
rosalind/problems/full

Given: a list 'L' containing 2n+3 positive real numbers. The first number in L
is the parent mass of peptide 'P', and all other numbers represent the masses
of some b-ions and y-ions of P (in no particular order). You may assume that
if the mass of a b-ion is present, then so is that of its complementary y-ion
and vice-versa.

Return: A protein string 't' of length n, for which there exist two positive
real numbers 'w1' and 'w2' such that for every prefix 'p' and suffix 's' of
't', each of w(p)+w1 and w(s)+w2 is equal to an element of L. In other words,
there exists a protein string whose t-prefix and t-suffix weights correspond
to the non-parent mass values in L.
"""

import numpy as np
from sys import argv
from mass_dict import get_mass_dict

mass_dict = get_mass_dict()

def parse_input(file_in):
    """return [parent, [ions]] from file-path"""
    return [float(i) for i in open(file_in)]


def find_nearest(array, value):
    """return element of array that is closest to value"""
    idx = np.abs(np.array(array) - value).argmin()
    return array[idx]


def find_match(parent, ions):
    """find pairs of b/y-ions that combine to equal parent mass"""
    pairs = []
    for ion in ions:
        diff = parent - ion
        pairs.append((ion, find_nearest(ions, diff)))
    return pairs


def remove_mirrors(l):
    """
    remove elements that are mirrors of existing elements
    i.e [(1, 3), (3, 1), (6, 2)] => [(1, 3), (6, 2)]
    """
    x = set()
    # I'm not even sorry for this one
    return [i for i in l if tuple(i[::-1]) not in x and not x.add(tuple(i))]


def mass_added(l):
    """return mass list for pairs of abs(b-ions - y-ions)"""
    return [abs(i[0] - i[1]) for i in sorted(l, key=lambda tup: tup[0])]


def full(file_in):
    """return protein string"""
    parent, *ions = parse_input(file_in)
    pairs = remove_mirrors(find_match(parent, ions))
    mass_list = mass_added(pairs)
    print(mass_list)
    seq = ""
    for i in range(1, len(mass_list)):
        current_mass = abs(mass_list[i] - mass_list[i-1])
        seq += mass_dict[round(current_mass, 3)]
    print(seq)


if __name__ == "__main__":
    full(argv[1])