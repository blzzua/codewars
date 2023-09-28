# https://www.codewars.com/kata/55688b4e725f41d1e9000065

def even_fib(n):
    a, b = 0, 1
    res = 0
    while b < n:
        if b % 2 == 0:
            res += b
        a, b = b, a + b
    return res
