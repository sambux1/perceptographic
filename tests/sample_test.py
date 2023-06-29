from load_tinyimagenet import load_dataset

category_ids, categories, images = load_dataset()

from PIL import Image

from average_hash_calculator import normalize_hex
from average_hash_calculator import average_of_hash

#test 1
print("normalized hex value of ffff: ",normalize_hex("ffff"))
print("normalized hex value of 0000: ",normalize_hex("0000"))
print("normalized hexe value of 00ff: ",normalize_hex("00ff"))
print("normalized hex value of ff00: ", normalize_hex("ff00"))

#full test

for img_category in images:
    image_arr = []
    for image in img_category:
        img = Image.open(image)
        image_arr.append(img)
    print(average_of_hash(image_arr))




