from load_tinyimagenet import load_dataset

category_ids, categories, images = load_dataset()

from PIL import Image

for img_category in images:
    for image in img_category:
        img = Image.open(image)