# https://www.codewars.com/kata/60512be8bbc51a000a83d767
# https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation
def operator(a, n, b):
    if n == 0:
        return b + 1
    if n == 1:
        return a + b
    if n == 2:
        return a * b
    if n == 3:
        return a ** b
    if n == 4:
        if b == 0:
            return 1
        return a **  operator(a, n, b - 1)
