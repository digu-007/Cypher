def keyGeneration(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3

    while (e < phi and phi % e == 0):
        e += 2

    d, cur = 0, 1
    over = 0
    while True:
        over += 1
        cur += phi
        if (cur % e == 0):
            d = cur // e
            break
        if over > 100000000:
            return (0, 0, 0)
        
    return (n, e, d)


def preComputeKey():
    # huge = (10000000000000000051, 2000000000000000057)
    return (20000000000000000672000000000000002907, 7, 17142857142857143422857142857142859543)
