'''
This is an image class so all perceptual hashes can take the same form of
input, and images can be automatically converted into the right form for a
given perceptual hash (hidden from the user).

To create an Image object, you must pass the filename of the image.

When passed into a perceptual hash function, it will be converted into
the image data type supported by the perceptual hash function.

There are 2 types of images currently supported as output:
    1) PIL.Image objects
    2) opencv image objects
'''

import PIL
import cv2


class Image:

    def __init__(self, filename):
        self.filename = filename
    
    # convert to PIL.Image
    def get_pil_image(self):
        return PIL.Image.open(self.filename)
    
    # convert to opencv image
    def get_cv2_image(self):
        img = cv2.imread(self.filename)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)