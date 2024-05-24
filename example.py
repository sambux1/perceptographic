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

import numpy as np
x1 = np.random.randint(0, 2, size=(3))
x2 = np.random.randint(0, 2, size=(3))
polynomial = perceptographic.pph.Polynomial(input_length=100, field_size=251, threshold=2)
y1 = polynomial.hash(x1)
y2 = polynomial.hash(x2)
print(y1)
print(y2)
polynomial.evaluate(y1, y2)