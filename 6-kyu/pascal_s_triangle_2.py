# https://www.codewars.com/kata/52945ce49bb38560fe0001d9

def pascal(p):
    line = [1]
    res  =  [line]
    for i in range(p-1):
        line = [1] + [a + b for a,b in zip(line,line[1:])] + [1]
        res.append(line)
    return res

# clever recursive with math.comb 
from math import comb
@lru_cache
def pascal(n):
  if n == 1:
    return [[1]]
  else:
    return [pascal(n - 1) + [[comb(n - 1, i) for i in range(n)]]
