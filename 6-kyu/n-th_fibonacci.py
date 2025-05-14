# https://www.codewars.com/kata/522551eee9abb932420004a0

def nth_fib(n):
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return a
