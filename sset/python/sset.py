#!/usr/bin/env python3

# rosalind/problems/sset

from sys import argv

n = int(open(argv[1]).read())

ans = 2**n % 1e6
print(int(ans))
