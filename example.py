import perceptographic

p = perceptographic.Perceptographic('phash', 'log_threshold', 256, 200, 1)
img = perceptographic.perceptual.Image('/home/sam/Downloads/carina-nebula.jpg')
h = p.hash(img)
print(h)

import numpy as np
x = np.random.randint(0, 2, size=(20))

'''
pph = perceptographic.pph.LogThreshold(20, 2)
pph.save_description()
print(pph.hash(x))
'''

pph2 = perceptographic.pph.LogThreshold()
print(pph2.hash(x))
