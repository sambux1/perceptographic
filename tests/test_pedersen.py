from unittest import TestCase
import numpy as np
import random
import galois

#TODO: this is messy, use modules
import sys
sys.path.append("") # this adds the project parent directory to path

import pedersen

class TestPedersen(TestCase):

    def setUp(self):
        self.security_parameters = [32, 36]
        self.input_length = 1024

    def test_homomorphism(self):
        for security_parameter in self.security_parameters:
            h = pedersen.generate_pedersen_hash_function(self.input_length, security_parameter)

            p, q, g = pedersen.get_parameters(security_parameter)
            gf = galois.GF(p)

            # 50 test values, doesn't need to use secure randomness
            for _ in range(50):
                x1 = np.array([random.randint(0, 1) for i in range(self.input_length)])
                x2 = np.array([random.randint(0, 1) for i in range(self.input_length)])
                
                diff = (x1 - x2) % q

                correct = h(diff)


                y1 = gf(h(x1))
                y2 = gf(h(x2))

                actual = y1 / y2

                self.assertEqual(type(correct), type(actual))

