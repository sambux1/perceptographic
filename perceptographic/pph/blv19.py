'''
An implementation of the robust PPH described in section 4.2.3 of 
the following paper by Boyle et. al.

https://eprint.iacr.org/2018/1158.pdf
'''

from perceptographic.pph import PPH
import math
import numpy as np

class BLV19(PPH):

    @staticmethod
    def calculate_output_length(n, d, beta, eps, lam):
        k = math.log2(1 / beta)

        n_prime = n / (k * beta)
        d_prime = ((1 - eps) * d) + ((1 + eps) * (d / k))
        eps_prime = 1 - ((1 - eps) * d / d_prime)

        candidate_1 = 0.1 * lam / (eps_prime**2)

        p = (d_prime * (1 - eps_prime)) / n_prime
        H_p = (-1 * p * math.log2(p)) - ((1 - p) * math.log2(1 - p))
        candidate_2 = (n_prime * 3 * math.e**2 * math.log(2) * H_p + 0.01 * lam) / eps_prime

        candidate_3 = 4 * beta * n_prime + 1
        
        m = max(candidate_1, candidate_2, candidate_3)
        return m
    
    @staticmethod
    def find_optimal_parameters(n, d, lam=256, beta_step=0.0001, eps_max=1, eps_step=0.0001):
        beta_max = 0.01
        
        optimal_m = n
        optimal_beta = 0
        optimal_eps = 0

        # loop over all possible values of beta
        beta = beta_step
        while beta < beta_max:
            eps = (1 - (1 / (math.log2(1 / beta))) / (1 + (1 / math.log2(1 / beta))))
            
            # loop over all possible values of epsilon
            while eps < eps_max:
                # calculate the output length for this set of parameters
                m = BLV19.calculate_output_length(n, d, beta, eps, lam)
                if m < optimal_m:
                    optimal_m = m
                    optimal_beta = beta
                    optimal_eps = eps
                
                eps += eps_step

            beta += beta_step
        
        return int(optimal_m), optimal_beta, optimal_eps

    def __init__(self, n=1024, d=100, beta=0.005, eps=0.8, lam=100):
        # paper suggests beta < 0.01 for conservative assumption
        if beta >= 0.01:    
            raise Exception('Beta value must be < 0.01. Larger values may be a security risk.')
        
        self.k = math.log2(1 / beta)
        min_eps = ((1 - 1/self.k) / (1 + 1/self.k))
        if eps <= min_eps:
            raise Exception('Epsilon value too small. For the given beta value, epsilon must be > ' + str(round(min_eps, 3)))

        n_prime = n / (self.k * beta)
        d_prime = (1 - eps) * d + (1 + eps) * (d / self.k)
        eps_prime = 1 - (1 - eps) * d / d_prime

        # 3 candidates for output length m, choose the max
        candidate_1 = 0.5 * lam / (eps_prime**2)
        p = d_prime * (1 - eps_prime) / n_prime
        H_p = -1 * p * math.log2(p) - (1 - p) * math.log2(1 - p)
        candidate_2 = (n_prime * 3 * math.e**2 * math.log(2) * H_p + 0.01 * lam) / eps_prime
        candidate_3 = 4 * beta * n_prime + 1
        print(candidate_1, candidate_2, candidate_3)
        m = max(candidate_1, candidate_2, candidate_3)
        print('m:', m)

        self.sample(round(n_prime), round(m), round(d_prime), eps_prime)
    
    def sample(self, n, m, t, eps):
        self.mu_1 = (m / 2) * (1 - math.exp(-2 * (1 - eps)))
        self.mu_2 = (m / 2) * (1 - math.exp(-2 * (1 + eps)))
        print('mu1:', self.mu_1)
        print('mu2:', self.mu_2)

        self.tau = (self.mu_1 + self.mu_2) / 2
        self.tau = round(self.tau)
        print('tau:', self.tau)
        
        # generate the random matrix where each value is 1 with probability (1/t) and 0 otherwise
        # generate random int in the range [0, t) and select the ones that equal 0
        mat = np.random.randint(0, t, size=(m, n))
        self.A = np.equal(mat, 0)
    
    def hash(self):
        x_prime = sparsify(x, self.k)
        return self.to_hex(np.mod(np.matmul(self.A, x_prime), 2))
    
    def evaluate(self):
        distance = np.count_nonzero(y1 != y2)
        return distance <= self.tau
    
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
