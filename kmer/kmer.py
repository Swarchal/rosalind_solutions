#!/usr/bin/env python3.6
from re import findall
from sys import argv
from itertools import product

seq = "".join(i.strip() for i in open(argv[1]).readlines()[1:])
all_kmers = ["".join(j) for j in product(["A", "C", "G", "T"], repeat=4)]
print(*map(lambda kmer: len(findall(f"(?={kmer})", seq)), all_kmers))

