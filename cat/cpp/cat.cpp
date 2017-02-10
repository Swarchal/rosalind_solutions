#include "fasta.h"
#include <iostream>
#include <string>
#include <map>

/* rosalind/cat
 * works but reaally slow for long sequences 
 */

// declare cat function
int cat(const std::string seq, int start, int end,
        std::map<char, char> bp_map,
        std::map<array<int, 2>, int> mem_map);


int calc_side_a(std::string seq, int start, int end, int i,
                std::map<array<int, 2>, int> mem_map,
                std::map<char, char> bp_map)
{   
    // index of start and end positions
    array<int, 2> idx_side_a = {start+1, i-1};

    if (mem_map.count(idx_side_a) > 0) {
        // if index already in cache, then return result
        return mem_map[idx_side_a];
    } else {
        // not calculated yet, so do this
        return cat(seq, start+1, i-1, bp_map, mem_map);
    }
}


int calc_side_b(std::string seq, int start, int end, int i,
                std::map<array<int, 2>, int> mem_map,
                std::map<char, char> bp_map)
{
    array<int, 2> idx_side_b = {start+1, i-1};
    if (mem_map.count(idx_side_b) > 0) {
        return mem_map[idx_side_b];
    } else {
        return cat(seq, i+1, end, bp_map, mem_map);
    }
}


int cat(const std::string seq, int start, int end,
        std::map<char, char> bp_map,
        std::map<array<int, 2>, int> mem_map)
{
    int total = 0;

    // if number of nucleotides after the split is odd,
    // then it's an invalid edge
    if ((start - end + 1) % 2 != 0) {
        return 0;
    }

    // if we reach this far, we can't split the sequence anymore and nothing
    // has gone wrong then we have a complete non-crossing graph
    if (end < 0 || start >= seq.length() || start >= end) {
        return 1;
    }
    
    char current_nuc = seq[start];
    char complement_nuc = bp_map[current_nuc];

    // iterate through nucleotides in steps of 2
    for (int i = start+1; i < end+1; i+=2)
    {
        if (seq[i] == complement_nuc) {
            /* check if we have already calculated value for index,
             * if not calculate it
             */
            int side_a = calc_side_a(seq, start, end, i, mem_map, bp_map);
            int side_b = calc_side_b(seq, start, end, i, mem_map, bp_map);

            // create index to store in cache map
            array<int, 2> idx_side_a = {start+1, i-1};
            array<int, 2> idx_side_b = {i+1, end};

            // store arrays and values in cache map
            mem_map[idx_side_a] = side_a;
            mem_map[idx_side_b] = side_b;
            
            // multiply as if any are 0, retrn zero, if both are 1 return 1
            total += (side_a * side_b) % 1000000;
        }
    }
    return total;
}


int main(int argc, char *argv[])
{
    std::map<char, char> bp_map;
        bp_map['G']='C'; bp_map['A']='U';
        bp_map['C']='G'; bp_map['U']='A';

    // pointer to storage map
    std::map<array<int, 2>, int> mem_map;

    std::string seq = parse_fasta(argv[1])[0];

    int answer = cat(seq, 0, seq.length()-1, bp_map, mem_map);
    std::cout << answer << "\n";

    return 0;
}

