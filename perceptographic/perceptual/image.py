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
import numpy as np


class Image:

    def __init__(self, filename=''):
        self.filename = filename
        
        # cached image objects
        self.pil_image = None
        self.cv2_image = None
    
    # convert to PIL.Image
    def get_pil_image(self):
        if self.pil_image is not None:
            return self.pil_image
        img = PIL.Image.open(self.filename)
        self.pil_image = img
        return img
    
    # convert to opencv image
    def get_cv2_image(self):
        if self.cv2_image is not None:
            return self.cv2_image
        img = cv2.imread(self.filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.cv2_image = img
        return img

    @staticmethod
    def generate_random():
        img_pixel_data = (np.random.rand(500, 500, 3) * 255).astype('uint8')

        # create the image object to return
        img = Image()
        # create the PIL image
        img.pil_image = PIL.Image.fromarray(img_pixel_data).convert('RGB')
        # create the cv2 image
        img.cv2_image = cv2.cvtColor(img_pixel_data, cv2.COLOR_RGB2BGR)

        return img