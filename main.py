import numpy as np
import galois
import imagehash
from PIL import Image
from ajtai import generate_ajtai_hash_function
from pedersen import generate_pedersen_hash_function

# input  : array of base 3 values
# outout : hex string
def base3_to_hex(x):
    base10 = 0
    for val in x:
        base10 *= 3
        base10 += val
    return hex(base10)

# input  : array of base n values
# outout : hex string
def base_n_to_hex(x, base):
    base_n = 0
    for val in x:
        base_n *= base
        base_n += val
    return hex(base_n)

n = 1093
t = 16
k = n - 2*t # 1061

# input should be a PIL Image object
def perceptographic(img):
    # percpetually hash the image
    phash = imagehash.phash(img, hash_size=34)

    # cut off part of the phash for now and flatten it
    x = phash.hash.flatten()[:1093].astype(int)

    # sample and call the homomorphic collision-resistant hash function
    g = generate_pedersen_hash_function(1093)
    gx = g(x)
    print(gx)
    return
    #TODO: fix this

    # create the Reed Solomon code and parity check matrix
    gf = galois.GF(3**7)
    rs = galois.ReedSolomon(n, k, field=gf)

    # find the result of applying the parity check matrix to the phash
    Px = np.matmul(rs.H.view(np.ndarray), x)
    Px = np.mod(Px, 3**7)

    gx_hex = base3_to_hex(gx.tolist())
    Px_hex = base_n_to_hex(Px.tolist(), 3**7)

    output = Px_hex + gx_hex[2:]
    return output


# TESTING CODE

img = Image.open('/home/sam/Pictures/carina-nebula.jpg')
print(perceptographic(img))