# rosalind.info/dbru

import os, sets, tables, strutils, sequtils


proc read_file(filepath: string): seq[string] =
  let f = open(filepath, fmRead)
  result = @[]
  for line in f.lines:
    result.add(line)


proc reverse(input_string: string): string =
  result = newString(input_string.len)
  for index, character in input_string:
    result[input_string.high - index] = character


proc reverse_complement(seq: string): string =
  let map_table = {'A': 'T',
                   'T': 'A',
                   'G': 'C',
                   'C': 'G'}.toTable
  result = newString(seq.len)
  for index, nucleotide in reverse(seq):
    result[index] = map_table[nucleotide]


proc join_strings(s: string): string =
  return "($#, $#)" % [s[0 .. ^2], s[1 .. ^1]]


proc make_graph(seqs: seq[string]): HashSet[string] =
  result = initSet[string]()
  for s in seqs:
    result.incl(join_strings(s))


let
  seqs = read_file(paramStr(1))
  all_seqs = concat(seqs, seqs.map(reverse_complement))
  graphs = make_graph(all_seqs)

for i in graphs:
  echo i

