def func(n, d, k, D):
    prob = 1
    for i in range(int(n*D/k)):
        prob *= (n-d-i)/(n-i)
    return prob

n = 2048
k = 32
D = 4
for d in range(50):
    p = func(n, d, k, D)
    ptotal = 1 - (1-p)**k
    print(d, ptotal)