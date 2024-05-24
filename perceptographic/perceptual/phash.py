# a wrapper for the phash algorithm
# https://github.com/JohannesBuchner/imagehash

from perceptographic.perceptual import Perceptual, Image
import math
import numpy as np
from imagehash import phash, ImageHash


class PHash(Perceptual):

    def __init__(self, hash_length):
        '''
        For phash, the hash length must be a square.
        If length is not a square, round up to next square and issue warning.
        '''
        hash_len_sqrt = math.sqrt(hash_length)
        if hash_len_sqrt.is_integer():
            self.hash_size = int(hash_len_sqrt)
        else:
            self.hash_size = math.ceil(hash_len_sqrt)
            print('Warning: phash hash_length must be a perfect square. Rounding up to the next perfect square.')
    
    # helper function to see which hash length is being used
    #   since parameter passed on creation may be modified
    def get_hash_length(self):
        # the length of the output is the square of the hash_size parameter
        return self.hash_size * self.hash_size

    # input is a perceptographic.Image object
    def hash(self, img, as_hex=False):
        img = img.get_pil_image()
        h = self.to_hex(phash(img, self.hash_size).hash)
        ret = self.to_np_binary(h) if as_hex is False else h
        return ret
    
    def evaluate(self, h1, h2, as_hex=False):
        if as_hex:
            h1 = self.to_np_binary(h1)
            h2 = self.to_np_binary(h2)
        assert(len(h1) == len(h2))
        return np.sum(h1 != h2)
