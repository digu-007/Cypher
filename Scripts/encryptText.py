from modularExponentiation import power


def encryptText(s, mod, p):
    
    i = 0
    ans = ""
    for ch in s:
        i += 1
        num = ord(ch)
        cur = str(power(num, p, mod) + i)
        ans += cur
        ans += ' '

    return ans
