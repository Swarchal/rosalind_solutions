from Bio import SeqIO
import numpy as np
from sys import argv

def parse_fasta(path):
    """return list of sequences from fasta file"""
    seqs = SeqIO.parse(open(path), "fasta")
    return [list(i.seq) for i in seqs]


def edit(s, t):
    """
    minimum edit distance between two strings using
    the Wagner-Fischer algorithm
    """
    len_s, len_t  = len(s), len(t) 
    d = np.zeros((len_s + 1, len_t + 1), dtype=int)
    # pad matrix borders with consecutive numbers
    d[:, 0] = range(len_s+1)
    d[0, :] = range(len_t+1)

    for i, si in enumerate(s, 1):
        for j, tj in enumerate(t, 1):
            if si != tj:
                # set to min of (upper, left, or upperleft) + 1
                d[i, j] = min(d[i, j-1] + 1,
                              d[i-1, j] + 1,
                              d[i-1, j-1] + 1)
            else:
                d[i, j] = d[i-1, j-1]
    return d[len_s, len_t]


def main():
    seqs = parse_fasta(argv[1])
    print(edit(*seqs))


if __name__ == '__main__':
    main()
