#!/usr/bin/env julia
# rosalind/corr
using FastaIO
using Iterators
using Combinatorics

get_seqs(path) = [i[2] for i in FastaIO.readfasta(path)]

hamming(s::String, t::String) = sum(i != j for (i, j) in zip(s, t))

function revc(seq::String)
    """reverse complement of a DNA sequence"""
    comp = Dict('G' => 'C', 'C' => 'G', 'T' => 'A', 'A' => 'T')
    return reverse(map(x -> comp[x], seq))
end


function find_correct_reads(seqs::Array{String, 1})
    """return array of correct sequences"""
    correct_seqs = Array{String, 1}()
    for pair in combinations(seqs, 2)
        s, t = pair
        if s == t || revc(s) == t
            push!(correct_seqs, s, t)
        end
    end
    return unique(correct_seqs)
end


function main()
    seqs = get_seqs(ARGS[1])
    correct = find_correct_reads(seqs)
    incorrect = setdiff(seqs, correct)
    out = Array{String, 1}()
    for pair in product(correct, incorrect)
        s, t = pair
        if hamming(s, t) == 1
            corr = t * "->" * s
            push!(out, corr)
        elseif hamming(revc(s), t) == 1
            corr = t * "->" * revc(s)
            push!(out, corr)
        end
    end
    for i in unique(out) println(i) end
end

main()
