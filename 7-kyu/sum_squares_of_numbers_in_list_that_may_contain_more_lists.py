# https://www.codewars.com/kata/57882daf90b2f375280000ad

def ravel(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return ravel(l[0]) + ravel(l[1:])
    return l[:1] + ravel(l[1:])

def sumsquares(l):
    return sum(x**2 for x in ravel(l))
