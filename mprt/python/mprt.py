#! /usr/bin/env python3.6
# rosalind.info/mprt

import re
import sys
import requests


def read_file(file_path):
    return open(file_path, "r").read().splitlines()


def get_fasta_from_id(uniprot_id):
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    fasta = requests.get(url).text.split("\n")[1:] # remove first line
    return "".join([line.strip() for line in fasta])


def find_motif(seq, motif="N[^P][ST][^P]", overlap=True):
    if overlap: # use a lookahead
        motif = f"(?={motif})"
    return [position.start()+1 for position in re.finditer(motif, seq)]


def main():
    uniprot_ids = read_file(sys.argv[1])
    for uniprot_id in uniprot_ids:
        fasta = get_fasta_from_id(uniprot_id)
        motifs = find_motif(fasta)
        if len(motifs) > 0:
            print(uniprot_id)
            print(*motifs)


if __name__ == "__main__":
    main()
