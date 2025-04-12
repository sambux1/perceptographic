from unittest import TestCase
import numpy as np
import random
from ecpy.curves import Curve, Point

import sys
sys.path.append("") # this adds the project parent directory to path

import perceptographic
from perceptographic.pph import log_threshold

class TestLogThreshold(TestCase):

    def setUp(self):
        pass
    
    # test the correctness of the homomorphic CRHF
    def test_hcrhf(self):
        input_length = 256

        # sample the Pedersen hash function
        hcrhf = log_threshold.generate_pedersen_hash_function(input_length)

        # generate two random inputs and take their difference
        x1 = np.random.randint(0, 2, input_length, dtype=np.int8)
        x2 = np.random.randint(0, 2, input_length, dtype=np.int8)
        diff = x1 - x2

        # hash the random inputs and their difference
        y1 = hcrhf(x1)
        y2 = hcrhf(x2)
        ydiff = hcrhf(diff)

        # make sure the homomorphism property holds
        self.assertTrue(ydiff == (y1 - y2))
    
    # test the correctness of the conversions between hex and ecpy.curves.Point
    def test_point_conversions(self):
        curve = Curve.get_curve('secp256k1')
        generator = curve.generator
        order = curve.order

        # test many to avoid probabilistic failures
        for i in range(1000):
            scaling_factor = random.randrange(0, order)
            point = scaling_factor * generator
            
            # point to hex and back to point
            h = log_threshold.point_to_hex(point)
            ret = log_threshold.hex_to_point(h)

            # check that result point is identical to original point
            self.assertTrue(point == ret)
    
    # test the correctness of the hash function
    def test_correctness(self):
        # sample a hash function
        input_length = 256
        threshold = 1
        pph = perceptographic.pph.LogThreshold(input_length, threshold)

        # generate a random input element
        x = np.random.randint(0, 2, size=(input_length))

        # generate an input element close to the original
        x_close = x.copy()
        flip_index = random.randint(0, input_length)
        x_close[flip_index] = 1 - x[flip_index]

        # generate an input one bit beyond the threshold
        x_far = x.copy()
        flipped_indices = []
        while len(flipped_indices) != threshold + 1:
            flip_index = random.randint(0, input_length)
            if flip_index in flipped_indices:
                continue
            x_far[flip_index] = 1 - x[flip_index]
            flipped_indices.append(flip_index)
        
        # hash all inputs
        y = pph.hash(x)
        y_close = pph.hash(x_close)
        y_far = pph.hash(x_far)

        # make sure the evaluations are correct
        self.assertTrue(pph.evaluate(y, y_close))
        self.assertFalse(pph.evaluate(y, y_far))
            