import galois
import numpy as np

# parameter n
n = 1093
k = 999

gf = galois.GF(3**7)

rs = galois.ReedSolomon(n, k, field=gf)

x = gf.Random(rs.n)
print(rs.H.shape)
print(x.shape)
Px = np.matmul(rs.H, x)
print(Px.shape)

Px = Px.view(np.ndarray)
print(np.mod(Px, 3))

# might be useful for syndrome list decoding
'''
print(rs.t)
print(rs.roots.size)
for root in rs.roots:
    print(root)
'''