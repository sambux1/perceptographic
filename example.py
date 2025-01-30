import perceptographic

p = perceptographic.Perceptographic('phash', 'log_threshold', 256, 200, 1)
img = perceptographic.perceptual.Image('/home/sam/Downloads/carina-nebula.jpg')
h = p.hash(img)
print(h)
