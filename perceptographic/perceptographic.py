'''
the main file for perceptographic hash functions

Takes as input a perceptual hash function and a PPH as objects.
'''

from perceptographic import perceptual
from perceptographic import pph


class Perceptographic:

    def __init__(self, perceptual_algorithm='phash', pph_algorithm='nonrobust',
                       perceptual_length=256, threshold=100, pph_length=64):
        # setup perceptual hash functtion
        # check if it is already an object, otherwise make the object
        if isinstance(perceptual_algorithm, perceptual.Perceptual):
            self.perceptual_algorithm = perceptual_algorithm
        else:
            self.perceptual_algorithm = perceptual.create(perceptual_algorithm, perceptual_length)
        
        # setup property-preserving hash function
        # check if it is already an object, otherwise make the object
        if isinstance(pph_algorithm, pph.PPH):
            self.pph_algorithm = pph_algorith
            print('got pph')
        else:
            self.pph_algorithm = pph.create(pph_algorithm, perceptual_length, pph_length, threshold)
    
    def hash(self, img):
        perceptual_hash = self.perceptual.hash(img)
        # convert to binarynumpy array
        return self.pph.hash(perceptual_hash)
    
    def evaluate(self, h1, h2):
        pass


if __name__ == '__main__':
    print('hey')