/* minimum edit distance between two strings
 * using the Wagner-Fischer algorithm */
#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include "fasta.h"
using namespace std;


void edit_dist(vector<string> seqs)
{
    assert(seqs.size() == 2);
    string s = seqs[0];
    string t = seqs[1];
    int len_s = s.size();
    int len_t = t.size();

    // create matrix of size 1:len(s)+1 by 1:len(t)+1
    vector<vector<int>> d(len_s+1, vector<int>(len_t+1));

    // make borders consectively numbered from 1:len_s and 1:len_t
    for (int i=0; i<=len_s; i++)
    {
        d[i][0] = i;
    }
    for (int j=0; j<=len_t; j++)
    {
        d[0][j] = j;
    }

    // loop through characters and fill matrix
    for (int i=1; i<=len_s; i++)
    {
        for (int j=1; j<=len_t; j++)
        {
            if (s[i-1] == t[j-1])
            {
                d[i][j] = d[i-1][j-1];
            } else
            {
                int left, upper, upperleft;
                left = d[i][j-1] + 1;
                upper = d[i-1][j] + 1;
                upperleft = d[i-1][j-1] + 1;
                d[i][j] = min(min(left, upper), upperleft);
            }
        }
    }
    cout << d[len_s][len_t] << "\n";
}



int main(int argc, char *argv[])
{
    vector<string> sequences = parse_fasta(argv[1]);
    edit_dist(sequences);
    return 0;
}
