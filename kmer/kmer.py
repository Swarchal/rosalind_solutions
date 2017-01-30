#!/usr/bin/env python3.6
# rosalind/kmer
import sys
import re
from itertools import product
from Bio import SeqIO

def count_kmer(string, kmer):
    """use regex lookaheads to count overlapping matches"""
    return len(re.findall(f"(?={kmer})", string))


def get_seq(path):
    """return single sequence from fasta"""
    fasta = SeqIO.parse(path, "fasta")
    for i in fasta:
        return str(i.seq)


def main():
    seq = get_seq(sys.argv[1])
    all_kmers = ["".join(i) for i in product(["A", "C", "G", "T"], repeat=4)]
    ans = [count_kmer(seq, kmer) for kmer in all_kmers]
    print(*ans)

if __name__ == "__main__":
    main()

