# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    res = 0
    while n >= 10:
        digits_prod = 1
        while n > 0:
            n, d  = divmod(n, 10)
            digits_prod *= d
        n = digits_prod
        res += 1
    return res
