#! /usr/bin/env python3.6

"""
roadlind.info/dbru
"""

import sys
import itertools

def read_file(filepath):
    return set(line.strip() for line in open(filepath, "r").readlines())


def reverse_complement(sequence):
    map_dict = {"A": "T",
                "T": "A",
                "G": "C",
                "C": "G"}
    new_sequence = ""
    for nucleotide in sequence:
        new_sequence += map_dict[nucleotide]
    return new_sequence[::-1] # [::-1] reverses iterables


def make_de_bruijn_graph(seqs):
    graph = set()
    for seq in seqs:
        graph.add((seq[:-1], seq[1:]))
    return graph


def pretty_print(graph):
    for seq1, seq2 in graph:
        print(f"({seq1}, {seq2})")


def main():
    sequences = read_file(sys.argv[1])
    revc_seqs = [reverse_complement(seq) for seq in sequences]
    graph = make_de_bruijn_graph(sequences)
    graph_revc = make_de_bruijn_graph(revc_seqs)
    pretty_print(graph | graph_revc)


if __name__ == "__main__":

    main()

