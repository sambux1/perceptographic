import galois
import random

#TODO: 1) pick actual final values

# each element has the form
# security_parameter -> [p, q, g]
parameters = dict([
    (32, [  4294967087,
            2147483543,
            2670277021]),
    (36, [  68719476599,
            34359738299,
            3863259943])
])
def get_parameters(security_parameter):
    #TODO: ensure security parameter is in the dictionary
    params = parameters[security_parameter]
    return params[0], params[1], params[2]


#TODO: secure source of randomness
def generate_random_group_elements(p, q, g, n):
    ret = []
    for i in range(n):
        r = random.randint(1, q)
        y = g**r
        ret.append(y)
    return ret

def generate_pedersen_hash_function(n, security):
    p, q, g = get_parameters(security)

    gf = galois.GF(p)
    g = gf(g)

    gs = gf(generate_random_group_elements(p, q, g, n))

    def h(x):
        ret = 1
        for i in range(n):
            val = gs[i] ** x[i]
            ret = val * ret
        return ret
    
    return h


# testing

n = 1024
h = generate_pedersen_hash_function(n, security=32)

import numpy as np

x1 = np.array([random.randint(0, 1) for i in range(n)])
x2 = np.array([random.randint(0, 1) for i in range(n)])

p, q, _ = get_parameters(32)
diff = (x1 - x2) % q
print(diff)

gf = galois.GF(p)

y1 = h(x1)
y2 = h(x2)
print('actual:', h(diff))

y1 = gf(y1)
y2 = gf(y2)
print('correct:', y1 / y2)
