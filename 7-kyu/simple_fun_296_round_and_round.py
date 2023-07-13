# https://www.codewars.com/kata/591e8c715b1d254f9e00005e

def round_and_round(n, a, b):
    res = (a + b ) % n
    if res > 0:
        return res
    else:
        return n
