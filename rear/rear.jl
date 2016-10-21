#!/usr/bin/env julia

# NOTE: not working
"""
Given a collection of 5 pairs of permutations, all of which have a length of 10
Return the reversal distance between each perumutation pair

e.g

1 2 3 4 5 6 7 8 9 10
3 1 5 2 7 4 9 6 10 8

9
"""

function reversal(seq, start, stop)
    """reverse array x between slice start to stop"""
    x = copy(seq)
    x[start:stop] = reverse(x[start:stop])
    return x
end


function inverse_permutation(x)
    a = zeros(length(x))
    for (i, n) in enumerate(x)
        a[n-1] = i+1
    end
    return a
end

x = readdlm(ARGS[1], Int)
