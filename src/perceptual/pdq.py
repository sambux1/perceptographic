# a wrapper for the PDQ algorithm (Facebook)
# https://github.com/faustomorales/pdqhash-python

from src.perceptual import Perceptual, Image

import pdqhash


class PDQ(Perceptual):

    def __init__(self):
        pass
    
    def hash(self, img):
        img = img.get_cv2_image()
        hash_vector, quality = pdqhash.compute(img)
        return hash_vector
    
    def evaluate(self, h1, h2):
        pass

if __name__ == '__main__':
    print('hey')
    pdq = PDQ()
    filename = '/home/sam/Downloads/carina-nebula.jpg'
    img = Image(filename)
    v = pdq.hash(img)
    print(v)

#TODO: figure out parameters