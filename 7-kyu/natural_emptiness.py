# https://www.codewars.com/kata/64b8c6c09416795eb9fbdcbf

def rep_set(n):
    if n == 0:
        return []
    else:
        return rep_set(n-1) + [rep_set(n-1)]



# clever and compact:
return [rep_set(x) for x in range(n)]

# best practice: using LRU
from functools import cache
@cache
def rep_set(n):


# precomputed solutions:
PRECOMPUTED = [[]]
for i in range(15):
    PRECOMPUTED.append([*PRECOMPUTED])

def rep_set(n):
    return PRECOMPUTED[n]
  
