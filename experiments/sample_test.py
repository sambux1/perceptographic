# this is necessary (temporarily) to be able to import the library
import sys
sys.path.insert(1, "../")

from load_tinyimagenet import load_dataset

category_ids, categories, images = load_dataset()

from PIL import Image
import perceptographic

for img_category in images:
    for image in img_category:
        # open as a PIL.Image object
        img_pil = Image.open(image)
        # or, more generally, open as a perceptographic.Image object that
        #   can be automatically converted to a PIL.Image object
        # (do this unless you have a reason not to)
        img = perceptographic.perceptual.Image(image)