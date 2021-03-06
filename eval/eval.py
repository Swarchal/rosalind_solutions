#!/usr/bin/env python3
"""
Given:  - an integer n
        - DNA string s, of even length up to 10bp
        - an array A, of length upto 10, floats between 0 and 1

Return : An array B, having the same length as A, in which B[i] represents
         the expected number of times that s will appear as a substring of a
         a random DNA string t of length n, where t is formed with GC-content
         A[i].
"""

import numpy as np
import sys

def parse_input(file_in):
    """parse input into list [n::int, s::str, A::list]"""
    out = [line.strip() for line in open(file_in)]
    out[0] = int(out[0])
    out[-1] = [float(i) for i in out[-1].split(" ")]
    return out


def prob_motif(gc_prop, s):
    """probability of a random motif given GC proportion"""
    gc = gc_prop / 2
    at = (1 - gc_prop) / 2
    nuc_dict = {"G":gc, "C":gc, "A":at, "T":at}
    return np.prod([nuc_dict[i] for i in s])


def _eval(n, s, A):
    """number of motifs given GC proportion"""
    return [prob_motif(i, s) * (n - 1) for i in A]
 

def main(file_in):
    """parse input file and calculate number B[i] for i in A"""
    input_list = parse_input(file_in)
    return _eval(*input_list)


if __name__ == "__main__":
    np.savetxt(sys.stdout.buffer, main(sys.argv[1]), fmt="%.3f", newline=" ")
