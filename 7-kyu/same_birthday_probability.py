# https://www.codewars.com/kata/5419cf8939c5ef0d50000ef2

from math import factorial
f365 = factorial(365)
def calculate_probability(n):
    if n > 365:
        return 1
    return round(1 - (f365 // factorial(365 - n)) / 365**n, 2)
