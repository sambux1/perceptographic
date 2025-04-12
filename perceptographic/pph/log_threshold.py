from perceptographic.pph import PPH
import perceptographic.common as common
import numpy as np
from itertools import combinations, product
import msgpack
import secrets
from ecpy.curves import Curve, Point


# sample a Pedersen hash function for input length n and return as a function
def generate_pedersen_hash_function(n):
    curve = Curve.get_curve('secp256k1')
    generator = curve.generator
    order = curve.order
    rand_scaling_constants = [secrets.randbelow(order) for i in range(n)]
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

    def __init__(self, input_length, threshold):
        self.input_length = input_length
        self.threshold = threshold
        self.sample()
        self.precompute_hash_list()

    def sample(self):
        self.pedersen = generate_pedersen_hash_function(self.input_length)

    def precompute_hash_list(self):
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

    def save_description(self):
        points_hex = [point_to_hex(p) for p in self.error_hashes if not p.is_infinity]

        with open("log_threshold.msgpack", "wb") as f:
            msgpack.pack(points_hex, f)
    
    def load_from_description(self):
        with open("log_threshold.msgpack", "rb") as f:
            points_hex = msgpack.unpack(f, raw=False)
            self.error_hashes = [hex_to_point(p) for p in points_hex]