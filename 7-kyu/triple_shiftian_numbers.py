# https://www.codewars.com/kata/56b7526481290c2ff1000c75

def triple_shiftian(base,n):
    c,b,a = base
    res = base[:]
    for i in range(n):
        n = 4*a-5*b+3*c
        res.append(n)
        c,b,a = res[-3:]
    return res[-3]

