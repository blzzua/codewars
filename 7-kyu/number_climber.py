# https://www.codewars.com/kata/559760bae64c31556c00006b

def climb(n):
    res = [n]
    while n > 1:
        n = n // 2
        res.append(n)
    return res[::-1]
