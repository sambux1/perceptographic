from perceptographic.pph import PPH
import perceptographic.common as common
import numpy as np


class HCRHF(PPH):

    def __init__(self, input_length):
        self.input_length = input_length
        self.sample()
        self.precompute_hash_table()

    def sample(self):
        self.pedersen = common.generate_pedersen_hash_function(self.input_length)

    def precompute_hash_table(self):
        self.error_hashes = []

        zeros = [0 for i in range(self.input_length)]
        self.error_hashes.append(self.pedersen(zeros))

        for i in range(self.input_length):
            error_vector_neg = zeros.copy()
            error_vector_pos = zeros.copy()
            error_vector_neg[i] = -1
            error_vector_pos[i] = +1
            self.error_hashes.append(self.pedersen(error_vector_neg))
            self.error_hashes.append(self.pedersen(error_vector_pos))

    def hash(self, x):
        return self.pedersen(x)
        #TODO: to hex and back
    
    def evaluate(self, y1, y2):
        #TODO: get points from hex
        y3 = y1 - y2
        for error in self.error_hashes:
            if y3 == error:
                print('MATCH FOUND')
