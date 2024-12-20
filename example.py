import perceptographic
'''
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
'''
'''
# test automatic parameter generation
print('(1024, 100) - 1.00: ', perceptographic.pph.BLV19.find_optimal_parameters(20000, 150, eps_max=1))
print('(1024, 100) - 0.95: ', perceptographic.pph.BLV19.find_optimal_parameters(20000, 150, eps_max=0.95))
print('(1024, 100) - 0.90: ', perceptographic.pph.BLV19.find_optimal_parameters(20000, 150, eps_max=0.90))
print('(1024, 100) - 0.85: ', perceptographic.pph.BLV19.find_optimal_parameters(20000, 150, eps_max=0.85))
robust = perceptographic.pph.BLV19(20000, 50, beta=0.0001, eps=0.9300097892905979)
'''
'''
import numpy as np
x1 = np.random.randint(0, 2, size=(3))
x2 = np.random.randint(0, 2, size=(3))
polynomial = perceptographic.pph.Polynomial(input_length=100, field_size=251, threshold=2)
y1 = polynomial.hash(x1)
y2 = polynomial.hash(x2)
print(y1)
print(y2)
polynomial.evaluate(y1, y2)


img1 = perceptographic.perceptual.Image('/home/sam/Downloads/snakes.jpg')
img2 = perceptographic.perceptual.Image('/home/sam/Downloads/carina-nebula.jpg')
pdq = perceptographic.perceptual.PDQ()
h1 = pdq.hash(img1, True)
h2 = pdq.hash(img2, True)
print(h1)
print(h2)
print(pdq.evaluate(h1, h2, True))

phash = perceptographic.perceptual.PHash(145)
h11 = phash.hash(img1, True)
h12 = phash.hash(img2, True)
print(h11)
print(h12)
print(phash.evaluate(h11, h12, True))

perceptographic.perceptual.Image.generate_random()

print(perceptographic.common.generate_ajtai_hash_function(1000, 100, 17))
'''

import numpy as np
n = 500
x1 = np.random.randint(0, 2, size=(n))
x2 = x1.copy()
x2[47] = 1 - x2[47]#np.random.randint(0, 2, size=(n))
print(x1.sum())
print(x2.sum())
x3 = x1 + x2

hcrhf = perceptographic.pph.HCRHF(n, 10, 1)
p1 = hcrhf.hash(x1)
p2 = hcrhf.hash(x2)
#p3 = hcrhf.hash(x3)

hcrhf.evaluate(p1, p2)
hcrhf.evaluate(p2, p1)

#p = perceptographic.Perceptographic('phash', 'hcrhf', 256, 200, 256)

#img = perceptographic.perceptual.Image('/home/sam/Pictures/carina-nebula.jpg')

#h = p.hash(img)
#print(p3)
#print(p1 + p2)