# https://www.codewars.com/kata/6469e4c905eaefffd44b6504

def reverse_number(n, b):
    if b == 1: return n
    base = b
    res = 0
    while n > 0:
        res = res * b + n % b
        n = n // base
    return res

