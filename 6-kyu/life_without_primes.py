# https://www.codewars.com/kata/59f8750ac374cba8f0000033

from gmpy2 import is_prime
CACHE = [0]

def solve(n):
    global CACHE
    ldprimes = ['2','3','5','7']
    if n + 1 < len(CACHE) :
        return CACHE[n+1]
    res = CACHE[-1]
    i = len(CACHE) - 1
    while i <=  n :
        res += 1
        if any(d in ldprimes for d in str(res)) or is_prime(res):
            continue
        CACHE.append(res)
        i += 1
    return res


