# https://www.codewars.com/kata/53907ac3cd51b69f790006c5

def triangle_type(*args):
    a, b, c = sorted(args)
    if c >= a + b:
        return 0
    if c ** 2 < a ** 2 + b ** 2:
        return 1
    if c ** 2 == a ** 2 + b ** 2:
        return 2
    if c ** 2 > a ** 2 + b ** 2:
        return 3
