# https://www.codewars.com/kata/5bc027fccd4ec86c840000b7

from math import log10, ceil
def solve(n):
    if n <= 0:
        return 0
    a = 10**(ceil(log10(n+1))-1)-1 
    acum = 0
    b = n - a
    while a + b > 0:
        a, d = divmod(a, 10)
        acum += d
        b, d = divmod(b, 10)
        acum += d
    return acum
