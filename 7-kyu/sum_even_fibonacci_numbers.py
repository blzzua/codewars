# https://www.codewars.com/kata/5926624c9b424d10390000bf

def SumEvenFibonacci(limit):
    a = 1
    b = 1
    res = 0
    while a <= limit:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res
