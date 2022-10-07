# https://www.codewars.com/kata/555de49a04b7d1c13c00000e

def add(*args):
    return round(sum(n/i for i, n in enumerate(args,1)))

