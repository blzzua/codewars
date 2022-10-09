# https://www.codewars.com/kata/58846d50f54f021d90000012

def rounding(n,m):
    if n % m == m/2:
        return n
    else:
        return m * round(n/m)
