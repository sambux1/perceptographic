'''
the main file for perceptographic hash functions

Takes as input a perceptual hash function and a PPH as objects.
'''

class Perceptographic:

    def __init__(self, perceptual='phash', pph='nonrobust',
                       perceptual_length=256, threshold=100, pph_length=64):
        # setup perceptual hash functtion
        self.perceptual = Perceptual.create(perceptual, perceptual_length)
        self.pph = pph
    
    def hash(self, img):
        perceptual_hash = self.perceptual.hash(img)
        # convert to bi arynumpy array
        return self.pph.hash(perceptual_hash)
    
    def evaluate(self, h1, h2):
        pass