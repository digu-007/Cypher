from modularExponentiation import power


def encryptText(s, mod, p):

    sz = len(str(mod))
    i = 0
    ans = ""
    for ch in s:
        i += 1
        num = ord(ch)
        cur = str(power(num, p, mod) + i)
        while len(cur) < sz:
            cur = '0' + cur
        ans += cur

    return ans
