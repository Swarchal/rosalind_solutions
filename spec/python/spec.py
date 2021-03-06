#!/usr/bin/env python3

from sys import argv

mass_dict = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
 }

# reverse to dictionary to {mass : aa}
mass_dict = {round(mass, 3) : aa for aa, mass in mass_dict.items()}

def main(path):
    """return protein sequence from mass spectrum"""
    mass_list = [float(i) for i in open(path).read().split()]
    seq = ""
    for i in range(1, len(mass_list)):
        current_mass = mass_list[i] - mass_list[i-1]
        seq += mass_dict[round(current_mass, 3)]
    print(seq)

if __name__ == "__main__":
    main(argv[1])
