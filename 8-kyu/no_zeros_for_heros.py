# https://www.codewars.com/kata/570a6a46455d08ff8d001002

def no_boring_zeros(n):
    if n == 0:
        return 0
    while n % 10 == 0:
        n = n // 10
    return n


