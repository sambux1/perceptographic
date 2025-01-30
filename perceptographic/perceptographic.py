'''
the main file for perceptographic hash functions

Takes as input either perceptual and pph objects or strings representing
which algorithms to use to create the objects.
'''

from perceptographic import perceptual
from perceptographic import pph


class Perceptographic:

    def __init__(self, perceptual_algorithm='phash', pph_algorithm='nonrobust',
                       perceptual_length=256, pph_length=64, threshold=100):
        # setup perceptual hash function
        # check if it is already an object, otherwise make the object
        if isinstance(perceptual_algorithm, perceptual.Perceptual):
            self.perceptual_algorithm = perceptual_algorithm
        else:
            self.perceptual_algorithm = perceptual.create(perceptual_algorithm, perceptual_length)
        
        # setup property-preserving hash function
        # check if it is already an object, otherwise make the object
        if isinstance(pph_algorithm, pph.PPH):
            self.pph_algorithm = pph_algorithm
        else:
            self.pph_algorithm = pph.create(pph_algorithm, perceptual_length, pph_length, threshold)
    
    def hash(self, img):
        h = self.perceptual_algorithm.hash(img)
        h_binary = self.perceptual_algorithm.to_np_binary(h)
        return self.pph_algorithm.hash(h_binary)
    
    def evaluate(self, h1, h2):
        pass
