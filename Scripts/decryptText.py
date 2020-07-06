from modularExponentiation import power


def decryptText(s, mod, p):
    
    i = 0
    ans = ""
    num = ""
    for ch in s:
        if ch == ' ':
            i -= 1
            cur = chr(power(int(num) + i, p, mod))
            ans += cur
            num = ""
        else:
            num += ch

    return ans
