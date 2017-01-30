#!/usr/bin/env python3.6
import re
from sys import argv
from itertools import product

def count_kmer(string, kmer):
    return len(re.findall(f"(?={kmer})", string))

def main():
    seq = "".join(i.strip() for i in open(argv[1]).readlines() if not i.startswith(">"))
    all_kmers = ["".join(j) for j in product(["A", "C", "G", "T"], repeat=4)]
    ans = [count_kmer(seq, kmer) for kmer in all_kmers]
    print(*ans)

if __name__ == "__main__":
    main()

