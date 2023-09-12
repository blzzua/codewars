# https://www.codewars.com/kata/5884731139a9b4b7a8000002

def candles(m, n):
    c = m
    left = m
    while left >= n:
        c += leftover // n
        left = sum(divmod(left, n))
    return c
