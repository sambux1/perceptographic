from unittest import TestCase
import numpy as np
import random

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