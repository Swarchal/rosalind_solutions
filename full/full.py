#!/usr/bin/env python3

"""rosalind/problems/full"""

from data import fetch_mass_dict
import itertools
from sys import argv

mass_dict = fetch_mass_dict()

def find_pairs(parent, ions):
    """find pairs of b-ion and y-ion that equal mass of parent"""
    pairs = []
    for b, y in itertools.product(ions, repeat=2):
        if (2 * b < parent) and (abs(parent - b - y) < 1e-3):
            pairs.append((b, y))
    return pairs


def flip_and_sort(pairs):
    """reverse b-ion/y-ion in first pair and sort the list on b-ion mass"""
    pairs[1] = tuple(reversed(pairs[1]))
    return sorted(pairs)


def b_ion_diff(b, c):
    """
    compare difference between two b-ions and determine if this difference
    close enough to match the mass of an amino acid.
    """
    diff = abs(b - c)
    for aa, mass in mass_dict.items():
        if abs(diff - mass) < 1e-3:
            return aa
    raise Exception()


def main():
    """return protein string"""
    parent, *ions = map(float, open(argv[1]))
    pairs = find_pairs(parent, ions)
    seq = ""
    n = (len(ions)-2) / 2
    while len(seq) < n:
        b1, b2 = pairs[0][0], pairs[1][0]
        try:
            seq += b_ion_diff(b1, b2) 
            pairs.pop(0)
            pairs = sorted(pairs)
        except:
            pairs = flip_and_sort(pairs)
    print(seq)

if __name__ == "__main__":
    main()
