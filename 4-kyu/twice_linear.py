# https://www.codewars.com/kata/5672682212c8ecf83e000050

# actually this is https://oeis.org/A002977
# Klarner-Rado sequence: a(1) = 1; subsequent terms are defined by the rule that if m is present so are 2m+1 and 3m+1.
# https://rosettacode.org/wiki/Klarner-Rado_sequence

# my solution with some precomputed rainbowtable
cache = dict({0: 1})
def precompute(n):
    h = cache
    j, k = 0, 0
    for i in range(1,n):
        x = 2 * h.get(j, 0) + 1
        y = 3 * h.get(k, 0) + 1
        h[i] = min(x, y)
        if h[i] == x:
            j += 1
        if h[i] == y:
            k += 1
precompute(100000)
def dbl_linear(n):
    if n in cache:
        return cache[n]
    raise ValueError(n)


# this kata can be done with heapq 
