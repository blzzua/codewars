# https://www.codewars.com/kata/596ddaccdd42c1cf0e00005c

def calc(a):
    s = 0
    for i,n in enumerate(a,1):
        if n > 0:
            n = n * n
        if i % 3 == 0:
            n = n * 3
        if i % 5 == 0:
            n = - n 
        s += n
    return s
