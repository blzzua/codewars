# https://www.codewars.com/kata/55c9172ee4bb15af9000005d

def count_odd_pentaFib(n):
    if n == 0: return 0
    PB = [0, 1, 1, 2, 4]
    a, b, c, d, e = PB
    res = 1
    for i in range(5, n + 1):
        a, b, c, d, e = b, c, d, e, (a + b + c + d + e)
        if e % 2 == 1:
            res += 1
        PB.append(e)
    return res
