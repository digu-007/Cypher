def keyGeneration(p, q):

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3

    while (e < phi and phi % e == 0):
        e += 2

    d, cur = 0, 1
    while True:
        cur += phi
        if (cur % e == 0):
            d = cur // e
            break

    return (n, e, d)