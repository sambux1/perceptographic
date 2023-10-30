'''
An implementation of the non-robust PPH described in section 4 of 
the following paper by Holmgren et. al.

https://eprint.iacr.org/2022/842.pdf
'''

from pph import PPH
import common
import numpy as np
import galois
import math


class TempNonRobust(PPH):
    
    def __init__(self, n, m, t, parameter=None):
        self.sample(parameter, n, m, t)
    
    def sample(self, parameter, n, m, t):
        self.A = self._generate_random_matrix(n, m)

        self.gf = galois.GF(2)
        self.k = n - 2*t
        self.bch = galois.BCH(n, self.k, field=self.gf)

        # determine the widths of the components for decoding
        self.bits_ax = m
        self.bits_px = 2*t
        self.len_ax_hex = math.ceil(m / 4)
    
    def hash(self, x):
        Ax = np.matmul(self.A, x)
        Ax = np.mod(Ax, 2)

        Px = np.matmul(self.bch.H.view(np.ndarray), x)
        Px = np.mod(Px, 2)

        Ax_hex = common.base_n_to_hex(Ax, 2)
        Px_hex = common.base_n_to_hex(Px, 2)
        return Ax_hex + Px_hex[2:]
    
    def evaluate(self, y1, y2):
        y1 = y1[2:]
        Ax1_hex = y1[:self.len_ax_hex]
        Px1_hex = y1[self.len_ax_hex:]
        Ax1 = np.asarray(common.hex_to_base_n(Ax1_hex, 2, self.bits_ax))
        Px1 = np.asarray(common.hex_to_base_n(Px1_hex, 2, self.bits_px))

        y2 = y2[2:]
        Ax2_hex = y2[:self.len_ax_hex]
        Px2_hex = y2[self.len_ax_hex:]
        Ax2 = np.asarray(common.hex_to_base_n(Ax2_hex, 2, self.bits_ax))
        Px2 = np.asarray(common.hex_to_base_n(Px2_hex, 2, self.bits_px))

        # calculate the syndrome and use it to find the error vector
        syndrome = np.mod(Px1 - Px2, 2)
        e = np.matmul(np.transpose(self.bch.H.view(np.ndarray)), syndrome)

        # determine if Ae = w1 - w2
        Ae = np.mod(np.matmul(self.A, e), 2)
        Ax_diff = np.mod(Ax1 - Ax2, 2)
        print(Ae)
        print(Ax_diff)

        return np.array_equal(Ae, Ax_diff)

    @staticmethod
    def _generate_random_matrix(n, m):
        return np.random.randint(0, 2, size=(m, n))


import random
if __name__ == '__main__':
    pph = NonRobust(1023, 10, 20)
    for j in range(5):
        x1 = np.random.randint(0, 2, size=(1023))
        x2 = np.copy(x1)
        # generate similar arrays
        for i in range(1): # number of elements to flip
            index = random.randint(0, len(x1)-1)
            x2[index] = 1 - x1[index]
        #x2 = np.random.randint(0, 2, size=(1023))
        y1 = pph.hash(x1)
        y2 = pph.hash(x2)
        print(pph.evaluate(y1, y2))