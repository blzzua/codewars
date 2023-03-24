# https://www.codewars.com/kata/56b12e3ad2387de332000041

def diff(arr):
    maxd = 0
    maxpair = False
    for c in arr:
        a,b =  map(int,c.split('-'))
        d = abs(a-b)
        if maxd < d:
            maxd = d
            maxpair = c
    return maxpair
