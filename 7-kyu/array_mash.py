# https://www.codewars.com/kata/582642b1083e12521f0000da

def array_mash(a, b):
    res = []
    for i,j in zip(a,b):
        res.append(i)
        res.append(j)
    return res

