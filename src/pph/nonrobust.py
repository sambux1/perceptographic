'''
An implementation of the non-robust PPH described in section 4.2.1 of 
the following paper by Boyle et. al.

https://eprint.iacr.org/2018/1158.pdf
'''

from pph import PPH
import math

class NonRobust(PPH):
    
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
    
    def hash(self, x):
        pass
    
    def evaluate(self, y1, y2):
        pass

    @staticmethod
    def _generate_random_weighted_matrix(n, m):
        return np.random.randint(0, 2, size=(m, n))

if __name__ == '__main__':
    pph = NonRobust(2048, 256, 100, 0.25)
    print(pph.mu_1)
    print(pph.mu_2)
    print(pph.tau)