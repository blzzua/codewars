# https://www.codewars.com/kata/590005bab7c61748c0000039/train/python

import math
def pascal_matrix(n):
    mid = (n+1) // 2
    res = []
    for line in range(0,mid):
        padding = [0] * (mid - line-1)
        triangle =  [math.comb(line,i) for i in range(line+1) ] 
        stripes = []
        for a in triangle:
            stripes.append(a)
            stripes.append(0)
        stripes.pop()
        res.append( padding + stripes  + padding)
    return res
