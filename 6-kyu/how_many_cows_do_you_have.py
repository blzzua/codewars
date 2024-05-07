# https://www.codewars.com/kata/58311536e77f7d08de000085
# see also https://oeis.org/A000930

def count_cows(n):
    if not isinstance(n, int):
        return None
    if n < 0:
        return None
    a, b, c, d = 1, 0, 0, 0
    while n > 0:
        d = d + c
        c = b
        b = a
        a = d
        n = n-1
    return a+b+c+d
        
