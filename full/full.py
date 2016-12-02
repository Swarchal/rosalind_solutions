#!/usr/bin/env python3

import data
from sys import argv

mass_dict = data.fetch_mass_dict()

def find_match(current, mass_list):
    """return first match from list of masses"""
    for i in mass_list:
        for aa, mass in mass_dict.items():
            if abs(mass - (i - current)) < 1e-3:
                return aa
    return "abort abort!"


def main():
    parent, current, *rest = map(float, open(argv[1]))
    seq = ""
    n = (len([current] + rest) - 2) / 2
    while len(seq) < n:
        tmp = find_match(current, rest)
        if tmp == "abort abort!":
            break
        else:
            seq += tmp
            current += mass_dict[tmp]
            print(current)
            rest = [i for i in rest if i - current > 0]
    print(seq)


if __name__ == "__main__":
    main()

