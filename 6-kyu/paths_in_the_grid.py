# https://www.codewars.com/kata/56a127b14d9687bba200004d

from math import comb
def number_of_routes(m, n):
    return comb(m+n, m)
