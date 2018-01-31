# rosalind.info/mprt

import httpclient, strutils, re, sequtils, os

proc read_file(file_path: string): seq[string] =
  # read in file, return sequence, an element per line
  result = @[]
  let file = open(file_path)
  for line in file.lines:
    result.add(line)


proc get_fasta(uniprot_id: string): string =
  # get fasta sequence from uniprot
  var
    url = "http://www.uniprot.org/uniprot/$#.fasta" % uniprot_id
    text = split_lines(newHttpClient().get_content(url))
  text.delete(0)
  return foldl(text, a&b)


proc find_motif(sequence: string,
                motif: Regex = re"(?=N[^P][ST][^P])"): seq[int] =
  # find motif positions in sequence using regex and lookaheads
  result = @[]
  var last_position = 0
  while last_position != -1:
    last_position = find(sequence, motif, start=last_position+1)
    if last_position != -1:
      result.add(last_position)
    # add 1 to positions (zero-indexed => 1-indexed)
  result = result.map(proc(x:int): int= x+1)


proc print(x: seq, sep: string = " ") =
  #print sequence with a separator
  for i in x:
    stdout.write i, sep


for motif in read_file(param_str(1)):
  var
    fasta = get_fasta(motif)
    output = find_motif(fasta)
  if len(output) != 0:
    echo motif
    print(output)
