#!/usr/bin/env julia
# rosalind/problems/long; assembling long reads
# FIXME works on example data, not on real dataset!!!

using FastaIO
using Combinatorics

read_fasta(path) = [i[2] for i in FastaIO.readfasta(path)]

function get_overlap(s, t)
    # return overlap of suffix of s to prefix of t; otherwise return nothing
    for i in 1:div(length(s), 2)
        s = s[2:end]
        t = t[1:end-1]
        if s == t
            return s # or t
        end
    end
end


function str_merge(s::String, t::String, o::String)
    # flatten two overlapping strings
    return s[1:rsearchindex(s, o)-1] * o * replace(t, o, "")
end

function all_pairs(collection)
    # return all pairs (including reversals)
    forward = collect(combinations(collection, 2))
    backward = collect(combinations(reverse(collection), 2))
    return vcat(forward, backward)
end


function ☹(reads)
    new_ans = []
    for (s, t) in all_pairs(reads)
        overlap = get_overlap(s, t)
        if overlap != nothing
            new_seqs = str_merge(s, t, overlap)
            push!(new_ans, new_seqs)
        end
    end
    return new_ans
end

reads = read_fasta(ARGS[1])

while length(reads) > 1
    reads = ☹(reads)
end

println(reads)