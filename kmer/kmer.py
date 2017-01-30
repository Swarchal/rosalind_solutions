#!/usr/bin/env python3
# rosalind/kmer

import sys
from itertools import product
from Bio import SeqIO

class string(str):
    """make my own string class that inherits str"""

    def count(self, substring):
        """count occurances of substring in string with overlaps"""
        count = start = 0
        while True:
            start = self.find(substring, start) + 1
            if start > 0:
                count += 1
            else:
                return count
        

def get_seq(path):
    """return single sequence from fasta"""
    fasta = SeqIO.parse(path, "fasta")
    for i in fasta:
        return string(i.seq) # custom class


def main():
    seq = get_seq(sys.argv[1])
    kmers = ["".join(i) for i in product(["A", "C", "G", "T"], repeat=4)]
    ans = [seq.count(j) for j in kmers]
    print(*ans)

if __name__ == "__main__":
    main()

