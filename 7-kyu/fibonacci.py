# https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af

def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

