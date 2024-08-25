# a file for general purpose functions that are useful for many constructions
import random
import numpy as np
from ecpy.curves import Curve, Point


'''
Conversions
'''
def np_binary_to_hex(x):
    return np.packbits(x).tobytes().hex()

def hex_to_np_binary(x):
    return np.unpackbits(np.frombuffer(bytes.fromhex(x), dtype=np.uint8))

'''
Ajtai Hash Function
(not currently used anywhere)
'''
def generate_ajtai_hash_function(n, m, q):
    # generate the matrix
    A = np.random.randint(1, q, size=(m, n))

    # create a callable function
    def h(x):
        y = np.matmul(A, x)
        return np.mod(y, q)

    return h

'''
Pedersen Hash Function
'''
def generate_pedersen_hash_function(n):
    curve = Curve.get_curve('secp256k1')
    generator = curve.generator
    order = curve.order
    rand_scaling_constants = [random.randrange(0, order) for i in range(n)]
    random_group_elements = []
    for const in rand_scaling_constants:
        random_group_elements.append(const * generator)
    
    # create a callable function
    def h(x):
        assert(len(x) == len(random_group_elements))

        ret = None
        for i in range(len(x)):
            point = x[i] * random_group_elements[i]
            
            if ret is None:
                ret = point
            else:
                ret = ret + point
        
        return ret
    
    return h

'''
Linear Algebra
'''
def _swap_rows(matrix, r1, r2):
    matrix[[r1, r2]] = matrix[[r2, r1]]

def gaussian_elimination(m):
    # assume augmentation of a square matrix
    assert(m.shape[0]+1 == m.shape[1])
    size = m.shape[0]

    pivot_row = 0
    pivot_col = 0
    while pivot_row < size and pivot_col < size:
        # pick the next pivot
        i_max = -1
        max_rest_of_col = 0
        for i in range(pivot_row, size):
            if abs(m[i, pivot_col]) > max_rest_of_col:
                i_max = i
                max_rest_of_col = abs(m[i, pivot_col])
        if i_max == -1:
            # can skip this column
            pivot_col += 1
            continue
        
        _swap_rows(m, pivot_row, i_max)
        # iterate over all rows after the pivot
        for i in range(pivot_row+1, size):
            scaling_constant = m[i, pivot_col] / m[pivot_row, pivot_col]
            m[i, pivot_col] = 0
            for j in range(pivot_col+1, size):
                m[i, j] = m[i, j] - (m[pivot_row, j] * scaling_constant)
        
        pivot_row += 1
        pivot_col += 1

    return m

def back_substitution(m):
    # assume augmentation of a square matrix
    assert(m.shape[0]+1 == m.shape[1])
    size = m.shape[0]
    
    # solution array
    solutions = np.zeros(size)
    
    # perform back substitution by working backward
    for i in range(size-1, -1, -1):
        solutions[i] = m[i, -1]  # Start with the augmented part
        for j in range(i+1, size):
            solutions[i] -= m[i, j] * solutions[j]
        solutions[i] /= m[i, i]
    
    return solutions
