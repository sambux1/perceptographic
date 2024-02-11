from unittest import TestCase
import numpy as np
import random

import sys
sys.path.append("") # this adds the project parent directory to path

#from nonrobust import NonRobust
import perceptographic


class TestPPH(TestCase):

    def setUp(self):
        pass
    
    def test_blv19_sparsification(self):
        k_vals = [4, 6, 8, 12, 16]
        sizes = [256, 512, 1024, 2048]
        for size in sizes:
            for k in k_vals:
                for i in range(100):
                    x1 = np.random.randint(0, 2, size=(size))
                    x2 = np.random.randint(0, 2, size=(size))
                    xdiff = np.logical_xor(x1, x2).sum()
                    y1 = perceptographic.pph.BLV19.sparsify(x1, k)
                    y2 = perceptographic.pph.BLV19.sparsify(x2, k)
                    ydiff = np.logical_xor(y1, y2).sum()
                    self.assertTrue(ydiff >= (2 * xdiff.sum() / k), "Sparsified vector is too sparse.")
                    self.assertTrue(ydiff.sum() <= (2 * xdiff.sum()), "Sparsified vector is not sparse enough.")

    '''
    def test_correctness(self):
        #TODO: this is pretty badly broken right now
        pph = NonRobust(2048, 256, 200, 0.25)

        count_true = 0
        # similar inputs, should evaluate to true
        for j in range(1000):
            x1 = np.random.randint(0, 2, size=(2048))
            x2 = np.copy(x1)
            # generate similar arrays with a certain number of differences
            for i in range(100): # number of elements to flip
                index = random.randint(0, len(x1)-1)
                x2[index] = 1 - x1[index]
            y1 = pph.hash(x1)
            y2 = pph.hash(x2)
            res = pph.evaluate(y1, y2)
            count_true += 1 if res is True else 0
        self.assertTrue(count_true > 950, count_true)
        
        # distant inputs, should evaluate to false
        count_false = 0
        for j in range(1000):
            x1 = np.random.randint(0, 2, size=(2048))
            x2 = np.copy(x1)
            # generate similar arrays with a certain number of differences
            for i in range(400): # number of elements to flip
                index = random.randint(0, len(x1)-1)
                x2[index] = 1 - x1[index]
            y1 = pph.hash(x1)
            y2 = pph.hash(x2)
            res = pph.evaluate(y1, y2)
            count_false += 1 if res is False else 0
        self.assertTrue(count_false > 950, count_false)
    '''