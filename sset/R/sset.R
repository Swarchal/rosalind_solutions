#! /usr/bin/env Rscript
# rosalind/problems/sset

input <- readLines(commandArgs(TRUE)[1])

n <- as.numeric(input)

print(2^n %% 1e6)
