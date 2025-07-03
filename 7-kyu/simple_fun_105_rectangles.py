# https://www.codewars.com/kata/589a8d9b729e7abd9a0000ed

from math import comb
def rectangles(n, m):
    return comb(n,2)*comb(m,2) # n*(n-1)*m*(m-1)//4
  
