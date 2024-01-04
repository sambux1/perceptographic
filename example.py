import perceptographic

p = perceptographic.Perceptographic('phash', 'nonrobust', 1600, 200, 256)

img = perceptographic.perceptual.Image('/home/sam/Pictures/carina-nebula.jpg')
h1 = p.hash(img)
h2 = p.hash(img)
print(h1)
print(h2)