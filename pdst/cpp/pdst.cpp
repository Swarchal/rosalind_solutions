// Rosalind pdst
//
// For a given FASTA file containing DNA sequences of the same length, return
// the distance matrix between all sequences.
// Distance should be defined as proportional distance, that is the hamming
// distance divided by the length of the string.

#include <string>
#include <iostream>
#include <cassert>
#include <vector>
#include <iomanip>
#include "fasta.h"
using namespace std;


float pdist(const string s1, const string s2)
{
    // proportional distance between two strings
    assert (s1.length() == s2.length());
    int total = 0;
    for (int i=0; i<s1.length(); i++)
    {
        if (s1[i] != s2[i])
        {
            total++;
        }
    }
    return (float) total / (float) s1.length();
}


vector<vector<float> > p_pdist(vector<string> x)
{
    // pairwise pdist between all pairs of strings
    // create 2D vector of size n*n
    int len = x.size();
    vector<vector<float> > mat(len, vector<float>(len));
    // pairs of strings in x
    for (int i=0; i<len; i++)
    {
        for (int j=0; j<len; j++)
	{
            mat[i][j] = pdist(x[i], x[j]);
        }
    }
    return mat;
}


int main(int argc, char *argv[])
{
    vector<string> sequences = parse_fasta(argv[1]);
    int len = sequences.size();
    vector<vector<float> > dist_matrix = p_pdist(sequences);
    // set printing precision to 4 decimal places
    cout << setprecision(4) << fixed;
    for (int i=0; i<len; i++)
    {
        for (int j=0; j<len; j++)
        {
            cout << dist_matrix[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
