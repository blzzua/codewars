# https://www.codewars.com/kata/588809279ab1e0e17700002e

from collections import Counter
from functools import lru_cache

@lru_cache(100000)
def s(x):
    return sum(map(int,str(x)))
    
def most_frequent_digit_sum(n):
    c = Counter()
    while n > 0:
        ds = s(n)
        c[ds] += 1
        n = n - ds
    top_cnt = c.most_common(1)[0][1]
    return max(key for key, cnt in c.items() if top_cnt  == cnt)

