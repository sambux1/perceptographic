import galois
import random

#TODO: 1) pick actual final values
#TODO: 2) create a list of parameter sets that can be easily selected from
p = 4294967087 #503
q = 2147483543 #251
g = 2670277021 #473

gf = galois.GF(p)
g = gf(g)


#TODO: secure source of randomness
def generate_random_group_elements(p, q, g, n):
    ret = []
    for i in range(n):
        r = random.randint(1, q)
        y = g**r
        ret.append(y)
    return gf(ret)

def generate_pedersen_hash(x):
    gs = generate_random_group_elements(p, q, g, 50)

    def h(x):
        ret = 1
        for i in range(n):
            val = gs[i] ** x[i]
            ret = val * ret
        return ret
    
    return h


# testing
'''
n = 50
h = generate_pedersen_hash(n)

import numpy as np

x1 = np.array([random.randint(1, q) for i in range(n)])
x2 = np.array([random.randint(1, q) for i in range(n)])

diff = (x1 - x2) % q

y1 = h(x1)
y2 = h(x2)
print('actual:', h(diff))

y1 = gf(y1)
y2 = gf(y2)
print('correct:', y1 / y2)
'''