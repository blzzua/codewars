# https://www.codewars.com/kata/5b752a42b11814b09c00005d

def solve(a,b):
    while a * b:
        if a >= 2 * b:
            a = a - 2 * b
        elif b >= 2 * a:
            b = b - 2 * a
        else:
            return [a,b]
    return [a,b]
