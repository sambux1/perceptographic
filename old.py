# get input
# should probably use python bytes data type - I think that's what other python hashes use

# make the bipartite expander graph
# this is the hardest part

# make the hash from the generated substrings

# n is the length of the input to the PPH
n = 2048
# t is the length of the CRHF output that is considered secure
t = 128
# k is the number of substrings to sample
k = 4 #temp
# kt is the output length of the hash
# kt < n is required for compression

# create the (n+k)(n+k) adjacency matrix, inefficient but works for now
import numpy as np
adj_matrix = np.zeros((n+k, n+k), dtype=int)
