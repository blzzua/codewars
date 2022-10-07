# https://www.codewars.com/kata/56e7d40129035aed6c000632

from math import comb
def easyline(n):
    return sum(comb(n,i)**2 for i in range(0,n+1))
    

