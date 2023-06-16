import numpy as np
# parameter k
# k >= 2 log_(3/e)m

# input length
l = 1024

# parameter t is the threshold
t = 100
# R is a family of t-wise independent hash functions

# ***** SAMPLING *****

# Steps:
# [done]  1) determine suitable values for k, p, m
# [done]  2) implement a family of t-wise independent hash functions, R
# [done]  3) sample k functions r_i from R

# generate a function from k-wise independent hash function family R
# p is prime modulus, m is number of buckets
# return value is a function
def generate_hash_function(k, p, m):
    a = np.random.randint(1, p, size=(k))
    
    def func(x):
        i = np.array([j for j in range(k)])
        x_arr = np.array([x for j in range(k)])
        powers = x_arr ** i
        products = a * powers
        return (np.sum(products) % p) % m
    
    return func

k = 200
m = 2 * l
p = 2**61 - 1
R = [generate_hash_function(k, p, m) for i in range(k)]

A = np.random.randint(0, p, size=(l, m))


# ***** HASHING *****
def encode(X):
    # X is a list
    H = np.zeros((l, k, 2*t))
    for x in X:
        for i in range(k):
            Ae = 0
            print(i)
            print(R[i](x))
            print(H[i, R[i](x)])

x = [np.random.randint(0, 2) for i in range(l)]
X = [2*i - x[i] for i in range(l)]

encode(X)