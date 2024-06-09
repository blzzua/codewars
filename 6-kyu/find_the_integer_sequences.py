# https://www.codewars.com/kata/582aad136755daf91a000021

def find_sequences(n):
    res = []
    a = 1
    b = 1
    sum_ = 1
    while b + 1 < n:
        #print(f'{a=}, {b=},  {sum_=}, {sum_ + b} >= {n}? {res=}')
        if sum_ + b >= n:
            sum_ -= a
            a += 1
        else:
            b += 1
            sum_ += b
            if sum_ == n:
                res.append(list(range(a, b + 1)))
    return sorted(res, key = lambda x: len(x))


# cool clever math method:
from math import isqrt
def find_sequences(n):
    res = []
    for a in reversed(range(1, n // 2 + 1)):
        c = n * 8 + (1 - 2 * a) ** 2
        d = isqrt(c)
        if d ** 2 != c:
            continue
        b = (d - 1) // 2
        res.append(list(range(a, b + 1)))
    return res

