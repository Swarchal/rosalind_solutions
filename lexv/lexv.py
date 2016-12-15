#!/usr/bin/env python3

"""rosalind/lexv"""

from itertools import combinations_with_replacement as combn
from itertools import permutations as perm
from sys import argv

def parse_input(file_in):
    """filename => [list(string), n]"""
    s, n = open(file_in, "r")
    return [s.split(), int(n)]


def make_permutations(s, n):
    """I'm not even sorry"""
    # make permutations
    out = [perm(x, len(x)) for l in range(n + 1) for x in combn(s, l)]
    # flatten list, remove duplicates and empty tuples
    set_list = set([i for s in out for i in s if i is not ()])
    # convert tuples to strings, pad to length n with empty spaces
    return ["".join(chars).ljust(n) for chars in set_list]


def score_permutations(permutation_list, s):
    """give each permutation a score, based on lexicographic order"""
    # create dictionary of {character => lexicographic score}
    score_dict = {ch : str(i).zfill(2) for i, ch in enumerate(list(" " + "".join(s)))}
    scores = []
    # loop through permutations, calculate score for each
    for i in permutation_list:
        string_score = ""
        for j in i:
            string_score += score_dict[j]
        scores.append(int(string_score))
    return zip(permutation_list, scores)


def sort_permutations(scored_list):
    """sort permutations based on their lexicographic score"""
    return sorted(scored_list, key=lambda x: x[1])


if __name__ == "__main__":
    string, n = parse_input(argv[1])
    permutations = make_permutations(string, n)
    scores = score_permutations(permutations, string)
    for i  in sort_permutations(scores):
        print(i[0].strip(" "))
