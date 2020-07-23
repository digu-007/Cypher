from modularExponentiation import power


def decryptText(s, mod, p):

    sz = len(str(mod))
    i = 0
    ans = ""
    num = ""
    s += ' '
    for ch in s:
        if len(num) == sz:
            i -= 1
            cur = chr(power(int(num) + i, p, mod))
            ans += cur
            num = ch
        else:
            num += ch

    return ans
