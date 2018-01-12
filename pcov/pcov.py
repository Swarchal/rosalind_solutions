"""
rosalind.info/problems/pcov

Given:
    A collection of (error-free) DNA k-mers (k≤50) taken from the same strand
    of a circular chromosome. In this dataset, all k-mers from this strand of
    the chromosome are present, and their de Bruijn graph consists of exactly
    one simple cycle.

Return:
    A cyclic superstring of minimal length containing the reads (thus
    corresponding to a candidate cyclic chromosome).

e.g
    input:
        ATTAC
        TACAG
        GATTA
        ACAGA
        CAGAT
        TTACA
        AGATT

    output:
        GATTACA
"""

import sys
import itertools

def read_file(filepath):
    return [line.strip() for line in open(filepath, "r")]


def is_edge(seq1, seq2):
    return seq1[1:] == seq2[:-1]


def join_seqs(seq1, seq2):
    return seq1[0] + seq2


def main():
    seqs = read_file(sys.argv[1])
    orig_length = len(seqs)
    for i in seqs:
        for j in seqs:
            if is_edge(i, j):
                new_seq = join_seqs(i, j)
                if len(new_seq) == orig_length:
                    print(new_seq)
                    break
                else:
                    seqs.append(new_seq)


if __name__ == "__main__":
    main()
