# https://www.codewars.com/kata/59c35ba16bddd219ee000082

def fibonacci(n):
    a, b = 1, 2
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def perimeter(n):
    f1 = fibonacci(n-1)
    f2 = fibonacci(n)
    return 2 * (f1 + f2)
