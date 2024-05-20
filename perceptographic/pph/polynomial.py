from perceptographic.pph import PPH
import math
import numpy as np


class Polynomial(PPH):
    
    def __init__(self, field_size=31, num_eval_points=5):
        self.field_size = field_size
        self.field_bitwidth = math.ceil(math.log2(self.field_size))
        self.num_eval_points = num_eval_points
        self.sample()
    
    # encode a bit string as a set
    # the output is a set with elements in the range [0, 2*x.size)
    @staticmethod
    def encode_as_set(x):
        # input should be a numpy.ndarray
        assert(isinstance(x, np.ndarray))

        encoding = set()
        for i in range(x.size):
            encoding.add(2*i - x[i] + 1)
        
        return encoding

    def sample(self):
        self.evaluation_points = np.random.randint(0, self.field_size, size=(self.num_eval_points))

    def evaluate_polynomial(self, roots, point):
        ret = 1
        for r in roots:
            ret *= (point - r)
            ret %= self.field_size
        return ret
    
    def hash(self, x):
        encoding = self.encode_as_set(x)
        output_bits = np.array([], dtype=int)
        for p in self.evaluation_points:
            y = self.evaluate_polynomial(encoding, p)
            y_bits = np.array([int(bit) for bit in bin(y)[2:].zfill(self.field_bitwidth)])
            output_bits = np.concatenate((output_bits, y_bits))
        return PPH.to_hex(output_bits)

    def evaluate(self, y1, y2):
        pass
