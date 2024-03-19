'''
Tests that all hashes take input and produce output of the correct types.
'''
from unittest import TestCase
import numpy as np

import sys
sys.path.append("") # this adds the project parent directory to path

import perceptographic


class TestTypes(TestCase):

    def setUp(self):
        # list of all perceptual and perceptographic hash functions that we want to test
        self.hash_functions = [
            perceptographic.perceptual.PHash(256),
            perceptographic.Perceptographic('phash', 'nonrobust', 1600, 200, 256)
        ]

    def test_correct_inputs(self):
        img = perceptographic.perceptual.Image('/home/sam/Pictures/carina-nebula.jpg')
        for hf in self.hash_functions:
            h = hf.hash(img)
            # check that the hash is a hex string
            self.assertTrue(isinstance(h, str), "hash is not a string")
            h_binary = perceptographic.perceptual.Perceptual.to_np_binary(h)
            self.assertTrue(isinstance(h_binary, np.ndarray), "hash cannot be converted to np.ndarray")