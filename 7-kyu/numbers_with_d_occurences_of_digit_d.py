# https://www.codewars.com/kata/5a40fc7ce1ce0e34440000a3

def is_dd(n):
    digits = {i: 0 for i in range(10)}
    while n > 0:
        n, d = divmod(n, 10)
        digits[d] += 1
    return any(digits[d] == d for d in digits if d)
