'''
An implementation of the robust PPH described in section 4.2.3 of 
the following paper by Boyle et. al.

https://eprint.iacr.org/2018/1158.pdf
'''

from perceptographic.pph import PPH
import math
import numpy as np

class BLV19(PPH):

    def __init__(self):
        pass
    
    def sample(self):
        pass
    
    def hash(self):
        pass
    
    def evaluate(self):
        pass
    
    # input x - a bit vector (np.ndarray)
    # input k - an integer specifying the block length which determines the sparseness
    @staticmethod
    def sparsify(x, k):
        num_blocks = math.ceil(len(x) / k)
        output = np.ndarray(shape=(num_blocks * 2**k), dtype=int)
        for i in range(num_blocks):
            # get the block of length k (can be smaller if it's the last block)
            y = x[k*i : k*(i+1)]

            t = 0
            for j in range(min(k, len(y))):
                t += (2**j * y[j])
            
            # get the t'th unit vector of length 2^k
            e_t = np.zeros(shape=(2**k))
            e_t[t] = 1

            # append the unit vector to the output vector by replacing the correct portion
            output[2**k * i : 2**k * (i+1)] = e_t
        
        return output
