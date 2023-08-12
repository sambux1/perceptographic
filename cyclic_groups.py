import random
import galois

q = 251
p = 503

gf = galois.GF(p)

# return x^y mod p (inefficiently)
def exp(x, y, p):
    ret = x
    for i in range(y-1):
        ret *= x
        ret %= p
    return ret

def mul(x, y, p):
    return x * y % p

potential_gs = []
for g in range(1, p):
    #if exp(g, q, p) == 1:
    g = gf(g)
    if g**q == 1:
        potential_gs.append(g)

g = potential_gs[random.randint(0, len(potential_gs)-1)]
print(g)

def generate_random_group_elements(p, q, g, n):
    ret = []
    for i in range(n):
        r = random.randint(1, q)
        y = g**r #exp(g, r, p)
        ret.append(y)
    return ret

elements = generate_random_group_elements(p, q, g, 10)
print(elements)

n = 10

def pedersen_hash(p, q, gs, n, x):
    ret = 1
    for i in range(n):
        val = gs[i]**x[i] #exp(gs[i], x[i], p)
        ret = val * ret #mul(ret, val, p)
    return ret

import numpy as np
x1 = np.array([random.randint(1, q) for i in range(n)])
x2 = np.array([random.randint(1, q) for i in range(n)])

diff = (x1 - x2) % q
print(diff)

y1 = pedersen_hash(p, q, elements, n, x1)
y2 = pedersen_hash(p, q, elements, n, x2)
print('actual:', pedersen_hash(p, q, elements, n, diff))

y1 = gf(y1)
y2 = gf(y2)
print('correct:', y1 / y2)