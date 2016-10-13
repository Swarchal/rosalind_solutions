#!/usr/bin/env python3
from sys import argv
import numpy as np
from Bio import SeqIO


def read_fasta(file_path):
    """ read fasta file """
    handle = open(file_path, "r")
    return [str(record.seq) for record in SeqIO.parse(handle, "fasta")]


def pdist(s1, s2):
    """ proportional distance between two strings """
    assert len(s1) == len(s2)
    return sum(i != j for i,j in zip(s1, s2)) / len(s1)


def pairwise_pdist(x):
    """ slow pairwise pdist between a list of strings """
    out = np.array([pdist(i, j) for i in x for j in x])
    out.shape = (len(x), len(x))
    return out


if __name__ == "__main__":
    seqs = read_fasta(argv[1])
    ans = pairwise_pdist(seqs)
    np.savetxt("ans.txt", ans, fmt='%2f', delimiter=' ')

