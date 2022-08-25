# https://www.codewars.com/kata/5b2117eea454c89d4400005f

# by recursive solution (as defined)

from functools import lru_cache
@lru_cache
def Ln(n, L0, L1, add):
    if n > 1:
        res = Ln(n-1, L0, L1, add) + Ln(n-2, L0, L1, add)+add
        return res
    elif n == 1:
        return L1
    elif n < 1:
        return L0

def L(n, L0, L1, add):
    return [Ln(i, L0, L1, add) for i in range(n)]
  

#  clever and best - iterative solution
def L(n, a,b,inc):
    lst = []
    for _ in range(n): 
        lst.append(a)
        a,b = b,a+b+inc
    return lst
