'''
An implementation of the non-robust PPH described in section 4.2.1 of 
the following paper by Boyle et. al.

https://eprint.iacr.org/2018/1158.pdf
'''

from src.pph import PPH
import math
import numpy as np


class Nonrobust(PPH):
    
    def __init__(self, n, m, t, eps=0.25):
        # epsilon and security parameter are dependent on each other
        #
        #   parameter = m * epsilon^2
        #
        # if epsilon is not specified, use default value
        self.sample(eps, n, m, t)
    
    def sample(self, eps, n, m, t):
        self.mu_1 = (m / 2) * (1 - math.exp(-2 * (1 - eps)))
        self.mu_2 = (m / 2) * (1 - math.exp(-2 * (1 + eps)))

        self.tau = (self.mu_1 + self.mu_2) / 2
        self.tau = round(self.tau)

        # generate the random matrix where each value is 1 with probability (1/t) and 0 otherwise
        # generate random int in the range [0, t) and select the ones that equal 0
        mat = np.random.randint(0, t, size=(m, n))
        self.A = np.equal(mat, 0)
    
    def hash(self, x):
        return np.mod(np.matmul(self.A, x), 2)
    
    def evaluate(self, y1, y2):
        distance = np.count_nonzero(y1 != y2)
        return distance <= self.tau

if __name__ == '__main__':
    pph = NonRobust(2048, 256, 100, 0.25)
    print(pph.mu_1)
    print(pph.mu_2)
    print(pph.tau)

    import random
    for j in range(5):
        x1 = np.random.randint(0, 2, size=(2048))
        x2 = np.copy(x1)
        # generate similar arrays
        for i in range(120): # number of elements to flip
            index = random.randint(0, len(x1)-1)
            x2[index] = 1 - x1[index]
        y1 = pph.hash(x1)
        y2 = pph.hash(x2)
        print(pph.evaluate(y1, y2))