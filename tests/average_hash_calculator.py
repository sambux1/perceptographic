import imagehash

def average_of_hash(image_arr):
    nor=0
    for image in image_arr:
        nor=nor+normalize_hex(imagehash.phash(image,7).__str__())
        #I am using 7 since max 8 digit hex could exceede max int value
    return nor/len(image_arr)


def normalize_hex(hex_value):
    max_value = int('F' * len(hex_value), 16)
    #use FFFF.... to represent the max value it could be
    decimal_value = int(hex_value, 16)
    normalized_value = decimal_value / max_value
    return normalized_value



