#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

vector<string> parse_fasta(const string file_path)
{
    ifstream input(file_path);
    if (!input.good()) {
        cerr << "ERROR: can't open file\n";
    }
    vector<string> fasta_out;
    string line, name, content, first_char;
    while (getline(input, line).good())
    {
        first_char = line[0];
        if (line.empty() || first_char == ">")
        {
            if (!name.empty())
            {
                fasta_out.push_back(content);
                name.clear();
            }
            if (!line.empty())
            {
                name = line.substr(1);
            }
            content.clear();
        } else if (!name.empty())
        content += line;
    }
    if (!name.empty())
    {
        fasta_out.push_back(content);
    }
    return fasta_out;
}
