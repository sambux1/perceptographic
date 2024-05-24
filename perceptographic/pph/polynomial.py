from perceptographic.pph import PPH
import perceptographic.common as common
import math
import numpy as np
import fractions


class Polynomial(PPH):
    
    def __init__(self, input_length, field_size=31, threshold=10):
        self.input_length = input_length
        self.field_size = field_size
        self.field_bitwidth = math.ceil(math.log2(self.field_size))
        self.threshold = threshold
        self.num_eval_points = 2 * self.threshold
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
        self.evaluation_points = np.random.randint(2 * self.input_length, self.field_size, size=(self.num_eval_points))

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
        return self.to_hex(output_bits)

    def evaluate(self, y1, y2):
        # get the bits of the hashes
        y1 = self.from_hex(y1)
        y2 = self.from_hex(y2)

        # get the evaluation points
        evaluated_points = []
        element_bitwidth = math.ceil(math.log2(self.field_size))
        for i in range(len(self.evaluation_points)):
            y1_point = 0
            y2_point = 0
            for j in range(element_bitwidth):
                y1_point = 2 * y1_point + y1[i*element_bitwidth + j]
                y2_point = 2 * y2_point + y2[i*element_bitwidth + j]
            fraction = fractions.Fraction(y1_point, y2_point)
            evaluated_points.append((self.evaluation_points[i], fraction))

        # construct matrix and vector for gaussian elimination
        matrix = np.zeros(shape=(2*self.threshold, 2*self.threshold))
        for row in range(2*self.threshold):
            for col in range(self.threshold):
                k_pow = pow(int(self.evaluation_points[row]), self.threshold-col-1, self.field_size)
                # left half of matrix
                matrix[row, col] = k_pow
                # right half of matrix
                matrix[row, self.threshold+col] = (-1 * evaluated_points[row][1]) * k_pow
        
        vector = np.zeros(shape=(2*self.threshold,))
        for row in range(2*self.threshold):
            k_pow = pow(int(self.evaluation_points[row]), self.threshold, self.field_size)
            vector[row] = (evaluated_points[row][1] * k_pow) - k_pow
        
        augmented_matrix = np.hstack((matrix, vector.reshape(-1, 1)))
        row_echelon_matrix = common.gaussian_elimination(augmented_matrix)
        solution_vector = common.back_substitution(row_echelon_matrix)
        print(solution_vector)
        p = pow(int(self.evaluation_points[0]), self.threshold, self.field_size)
        for i in range(self.threshold-1):
            p += solution_vector[i] * pow(int(self.evaluation_points[0]), self.threshold-i-1)
            p = p % self.field_size
        p += solution_vector[self.threshold-1]
        print(p)
        q = pow(int(self.evaluation_points[0]), self.threshold, self.field_size)
        for i in range(self.threshold-1):
            q += solution_vector[self.threshold+i] * pow(int(self.evaluation_points[0]), self.threshold-i-1)
            q = q % self.field_size
        q += solution_vector[-1]
        print(q)
        print(p/q)
        print(evaluated_points[0])
        # DOESNT WORK

