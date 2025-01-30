from perceptographic.pph import PPH
import perceptographic.common as common
import numpy as np
import random
from itertools import combinations, product
from ecpy.curves import Curve, Point


# sample a Pedersen hash function for input length n and return as a function
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

# helper function to convert an ecpy.curves.Point to hex
def point_to_hex(point):
    assert(isinstance(point, Point))
    x = hex(point.x)
    y = hex(point.y)
    return x + y[2:]    # ignore the leading '0x' of the second string

# helper function to convert a hex string to an ecpy.curves.Point
def hex_to_point(h):
    assert(isinstance(h, str))
    h = h[2:]   # ignore the leading '0x'

    # separate the hex into the x and y coordinates
    half_bitwidth = int(len(h) / 2)
    x = h[: half_bitwidth]
    y = h[half_bitwidth :]
    
    # convert hex strings to integers
    x = int(x, 16)
    y = int(y, 16)

    # create point from coordinates
    curve = Curve.get_curve('secp256k1')
    return Point(x, y, curve)


class LogThreshold(PPH):

    def __init__(self, input_length, output_length, threshold):
        self.input_length = input_length
        self.output_length = output_length
        self.threshold = threshold
        self.sample()
        self.precompute_hash_table()

    def sample(self):
        self.pedersen = generate_pedersen_hash_function(self.input_length)

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
        h = self.pedersen(x)
        return point_to_hex(h)
    
    def evaluate(self, y1, y2):
        y1 = hex_to_point(y1)
        y2 = hex_to_point(y2)
        
        y3 = y1 - y2
        for error in self.error_hashes:
            if y3 == error:
                return True

        return False
