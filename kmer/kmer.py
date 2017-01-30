#!/usr/bin/env python3.6
import re
from sys import argv
from itertools import product

count = lambda seq, kmer: len(re.findall(f"(?={kmer})", seq))

def main():
    seq = "".join(i.strip() for i in open(argv[1]).readlines()[1:])
    all_kmers = ["".join(j) for j in product(["A", "C", "G", "T"], repeat=4)]
    ans = [count(seq, kmer) for kmer in all_kmers]
    print(*ans)

if __name__ == "__main__":
    main()

