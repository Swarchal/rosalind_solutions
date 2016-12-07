#! /usr/bin/env python3

import numpy as np
import itertools
from sys import argv
from data import fetch_mass_dict

mass_table = fetch_mass_dict()

def mass_lookup(mass_list, tol=1e-3):
    """
    given a list of masses, this will return the first amino acid that
    has a mass within tolerance, and the index of that amino acid
    """
    for ion, weight in mass_table.items():
        for i, mass in enumerate(mass_list):
            if abs(mass - weight) < tol:
                return [i, ion]


def diff(L):
    """
    find first mass diff that matches an aa mass
    Returns: [aa, [truncated_list]]
    """
    *rest, top = L
    diffs = [top - i for i in rest]
    i, aa = mass_lookup(diffs)
    return [aa,  L[:i+1]]


def main():
    L = sorted([float(i) for i in open(argv[1])])
    seq = ""
    while len(L) >= 2:
        aa, L = diff(L)
        seq += aa
    print(seq[::-1])
 

if __name__ == "__main__":
    main()
