def power(n, p, mod):
    
    ans = 1
    while p > 0:
        if (p & 1):
            ans = (ans * n) % mod
        n = (n * n) % mod
        p >>= 1

    return ans
