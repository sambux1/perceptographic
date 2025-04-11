import perceptographic

p = perceptographic.Perceptographic('phash', 'log_threshold', 256, 200, 1)
img = perceptographic.perceptual.Image('/home/sam/Downloads/carina-nebula.jpg')
h = p.hash(img)
print(h)
#p.pph_algorithm.save_description()

pph = perceptographic.pph.LogThreshold(100, 1)
pph.save_description()
pph.load_from_description()