#!/usr/bin/env julia
using FastaIO

function parse_fasta(path)
    # return array of sequences
    return [i[2] for i in readfasta(path)]
end


function edit_dist(s::String, t::String)
    d = zeros(Int64, length(s)+1, length(t)+1)
    d[1, :] = range(1, length(s)+1)
    d[:, 1] = range(1, length(t)+1)
    @inbounds # speeeed!
    for i, si, in enumerate(s)
        for j, tj in enumerate(t)
            if si != tj
                d[i+1, j+1] = minumum(d[i+1, j]+1,
                                      d[i, j+1]+1,
                                      d[i, j] + 1)
            else
                d[i+1, j+1] = d[i, j]
            end
        end
    end
    return d[length(s)+1, length(t)+1]
end


function main()
    s, t = parse_fasta(ARGS[1])
    print(edit_dist(s, t))
end

main()
