# a wrapper for the phash algorithm
# https://github.com/JohannesBuchner/imagehash

from perceptual import Perceptual
import math
from PIL import Image

from imagehash import phash


class PHash(Perceptual):

    def __init__(self, hash_length):
        '''
        for phash, the hash length must be a square
        if length is not a square, round up to next square and issue warning
        '''
        hash_len_sqrt = math.sqrt(hash_length)
        if hash_len_sqrt.is_integer():
            self.hash_size = int(hash_len_sqrt)
        else:
            self.hash_size = math.ceil(hash_len_sqrt)
            print('Warning: phash hash_length must be a perfect square. Rounding up to the next perfect square.')
    
    # helper function to see which hash size is being used
    #   since parameter passed on creation may be modified
    def get_hash_size(self):
        return self.hash_size

    # input is a PIL.Image object
    def hash(self, img):
        return phash(img, self.hash_size)
    
    def evaluate(self, h1, h2):
        pass


if __name__ == '__main__':
    print("hey")
    img = Image.open('/home/sam/Downloads/carina-nebula.jpg')
    p = PHash(145)
    h = p.hash(img)
    print(p.get_hash_size())
    print(h)