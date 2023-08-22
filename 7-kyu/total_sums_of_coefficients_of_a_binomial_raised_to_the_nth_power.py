# https://www.codewars.com/kata/584a6d9d7d22f8fa09000094

def f(n):
    res = [2**i for i in range(n+1)]
    return res + [sum(res)]
