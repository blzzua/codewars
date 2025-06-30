# https://www.codewars.com/kata/5274d9d3ebc3030802000165

from math import gcd
def nbr_of_laps(x, y):
    return (y // gcd(x, y) , x // gcd(x, y))

