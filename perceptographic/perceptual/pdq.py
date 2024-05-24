# a wrapper for the PDQ algorithm (Facebook)
# https://github.com/faustomorales/pdqhash-python
# PDQ only supports 256 bit output

from perceptographic.perceptual import Perceptual, Image
import numpy as np
import pdqhash


class PDQ(Perceptual):

    def __init__(self):
        # PDQ does not allow parameters
        pass
    
    # always 256 for PDQ
    def get_hash_length(self):
        return 256
    
    def hash(self, img, as_hex=False):
        img = img.get_cv2_image()
        hash_vector, quality = pdqhash.compute(img)
        ret = hash_vector if as_hex is False else self.to_hex(hash_vector)
        return ret
    
    def evaluate(self, h1, h2, as_hex=False):
        if as_hex:
            h1 = self.to_np_binary(h1)
            h2 = self.to_np_binary(h2)
        assert(len(h1) == len(h2))
        return np.sum(h1 != h2)
