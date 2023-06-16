# implementation of Ajtai's hash function

import numpy as np

def generate_ajtai_hash_function(n, m, q):
    # generate the matrix
    A = np.random.randint(1, q, size=(m, n))

    # create a callable function
    def h(x):
        y = np.matmul(A, x)
        return np.mod(y, q)
    
    return h


# testing code
'''
h = generate_ajtai_hash_function(100, 10, 61)
x = np.random.randint(0, 2, size=(100))
y = h(x)
print(y)
'''