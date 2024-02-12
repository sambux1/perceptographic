import perceptographic

p = perceptographic.Perceptographic('phash', 'nonrobust', 1600, 200, 256)

img = perceptographic.perceptual.Image('/home/sam/Pictures/carina-nebula.jpg')
h1 = p.hash(img)
h2 = p.hash(img)
print(h1)
print(h2)

import numpy as np
x = np.random.randint(0, 2, size=(2048))
#print(x)
out = perceptographic.pph.BLV19.sparsify(x, 16)
#print(out)
print(len(out))

robust = perceptographic.pph.BLV19(2048, 80, beta=0.002, eps=0.963)