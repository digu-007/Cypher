import math


def checkPrime(n):
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqr = int(math.sqrt(n)) + 1
    for i in range(3, sqr, 2):
        if n % i == 0:
            return False
    
    return True
    