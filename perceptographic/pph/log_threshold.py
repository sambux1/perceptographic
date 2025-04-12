from perceptographic.pph import PPH
import perceptographic.common as common
import numpy as np
from itertools import combinations, product
import msgpack
import importlib.resources
import concurrent.futures
import os
import secrets
from ecpy.curves import Curve, Point


# sample a Pedersen hash function for input length n and return as a function
def generate_pedersen_hash_function(n, group_elements=None):
    random_group_elements = []

    if group_elements is not None:
        random_group_elements = group_elements
    else:
        curve = Curve.get_curve('secp256k1')
        generator = curve.generator
        order = curve.order
        rand_scaling_constants = [secrets.randbelow(order) for i in range(n)]
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
    
    return h, random_group_elements

# helper function to convert an ecpy.curves.Point to hex
def point_to_hex(point):
    assert(isinstance(point, Point))
    # pad to 64 hex chars to avoid dropping leading zeros
    x = format(point.x, '064x')
    y = format(point.y, '064x')
    return x + y

# helper function to convert a hex string to an ecpy.curves.Point
def hex_to_point(h):
    assert(isinstance(h, str))

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

    def __init__(self, input_length=None, threshold=None):
        # default constructor (or incomplete constructor) loads from description
        if input_length is None or threshold is None:
            self.load_from_description()
        else:
            self.input_length = input_length
            self.threshold = threshold
            self.sample()
            self.precompute_hash_list()

    def sample(self):
        self.pedersen, self.pedersen_elements = generate_pedersen_hash_function(self.input_length)

    def precompute_hash_list(self):
        zeros = [0 for i in range(self.input_length)]

        strings_to_hash = []

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
                    strings_to_hash.append(error_vector)
                
        # compute outside the for loop to allow for future threading
        self.error_hashes = [self.pedersen(v) for v in strings_to_hash]
        
        # append the hash of the zero error vector
        self.error_hashes.append(self.pedersen(zeros))

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

    def save_description(self):
        pedersen_points_hex = [point_to_hex(p) for p in self.pedersen_elements if not p.is_infinity]
        error_points_hex    = [point_to_hex(p) for p in self.error_hashes if not p.is_infinity]

        description = {
            'input_length': self.input_length,
            'threshold': self.threshold,
            'pedersen': pedersen_points_hex,
            'hash_list': error_points_hex
        }

        with open("perceptographic/data/log_threshold.msgpack", "wb") as f:
            msgpack.pack(description, f)
    
    def load_from_description(self):
        with open("perceptographic/data/log_threshold.msgpack", "rb") as f:
            description = msgpack.unpack(f)
        
        self.input_length = description['input_length']
        self.threshold    = description['threshold']
        self.pedersen_elements = [hex_to_point(p) for p in description['pedersen']]
        self.error_hashes      = [hex_to_point(p) for p in description['hash_list']] + [Point.infinity()]
        self.pedersen, _ = generate_pedersen_hash_function(self.input_length, self.pedersen_elements)
