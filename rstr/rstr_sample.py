#!/usr/bin/env python3
from sys import argv
from random import choice

# random sampling method
# entirely idiotc

def parse_input(input_file):
    """return [N, x, s]"""
    with open(input_file) as f:
        lines = f.readlines()
    N, x = lines[0].split()
    s = lines[1].strip()
    return [int(N), float(x), str(s)]


def gc_prop(s):
    return sum(s.count(i) for i in "GC")/len(s)


def generate_str(length, x):
    """generate random DNA string of length with a GC proportion of x"""
    # FIXME this can loop forever if GC proportion of individual strings cannot
    # equal x
    gc = False
    while gc == False:
        seq = ""
        for i in range(length):
            seq += choice("ACGT")
        gc = gc_prop(seq) == x
    return seq


def generate_seqs(N, length, gc_prop):
    """generate N random DNA strings with a GC proportion of x"""
    seqs = []
    for i in range(N):
        seqs.append(generate_str(length, gc_prop))
    return seqs


def main(N, x, s, n_iters=1000):
    """proportion we find string `s` in randomly generated sequences"""
    is_in = [s in generate_seqs(N, len(s), x) for i in range(n_iters)]
    prop = sum(is_in) / len(is_in)
    return prop


if __name__ == "__main__":
    # N, x, s = parse_input(argv[1])
    # repeat this many times, find proportion of the times that s in in seqs
    N = 10
    x = 0.6
    s = "ATAGCCGA"
    seqs = generate_seqs(N, len(s), x)
    print(seqs)