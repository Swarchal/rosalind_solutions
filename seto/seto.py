#!/usr/bin/env python3
"""
Given a positive integer `n` and two subsets `A` and `B`
of {1, 2,...,n}

Return six sets:
    1. A ∪ B
    2. A ∩ B
    3. A - B
    4. B - A
    5. A^c
    6. B^c
"""

import sys

def read_input_from_file(path):
    """return [n, A, B]"""
    with open(path, "r") as f:
        return list(map(eval, f.readlines()))




if __name__ == "__main__":
    n, A, B = read_input_from_file(sys.argv[1])
    U = set(range(1, n+1))

    print(A.union(B))
    print(A.intersection(B))
    print(A - B)
    print(B - A)
    print(U - A)
    print(U - B)

