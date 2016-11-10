#!/usr/bin/env julia
using FastaIO

function parse_fasta(path)
    # return array of sequences
    return [i[2] for i in readfasta(path)]
end


function edit_dist(s::String, t::String)
    d = zeros(Int64, length(s)+1, length(t)+1)
    d[1, :] = range(0, length(t)+1)
    d[:, 1] = range(0, length(s)+1)
    for i in range(1, length(s))
        for j in range(1, length(t))
            if s[i] != t[j]
                d[i+1, j+1] = minimum([d[i+1, j]+1,
                                       d[i, j+1]+1,
                                       d[i, j]+1])
            else
                d[i+1, j+1] = d[i, j]
            end
        end
    end
    return d[length(s)+1, length(t)+1]
end


function main()
    a, b = parse_fasta(ARGS[1])
    println(edit_dist(a, b))
end

main()
