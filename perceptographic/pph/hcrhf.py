from perceptographic.pph import PPH
import perceptographic.common as common
import numpy as np
from itertools import combinations, product


class HCRHF(PPH):

    def __init__(self, input_length, output_length, threshold):
        self.input_length = input_length
        self.output_length = output_length
        self.threshold = threshold
        self.sample()
        self.precompute_hash_table()

    def sample(self):
        self.pedersen = common.generate_pedersen_hash_function(self.input_length)

    def precompute_hash_table(self):
        self.error_hashes = []

        # append the hash of the zero error vector
        zeros = [0 for i in range(self.input_length)]
        self.error_hashes.append(self.pedersen(zeros))

        # iterate over all error vector hamming weights
        for weight in range(1, self.threshold + 1):
            # iterate over all combinations of error indices with the given hamming weight
            for indices in combinations(range(self.input_length), weight):
                # iterate over all combinations of signs
                for signs in product([1, -1], repeat=weight):
                    # construct the error vector
                    error_vector = zeros.copy()
                    for index, sign in zip(indices, signs):
                        error_vector[index] = sign
                    self.error_hashes.append(self.pedersen(error_vector))

    def hash(self, x):
        return self.pedersen(x)
        #TODO: to hex and back
    
    def evaluate(self, y1, y2):
        #TODO: get points from hex
        y3 = y1 - y2
        for error in self.error_hashes:
            if y3 == error:
                print('MATCH FOUND')
                return

        print('no match found')
