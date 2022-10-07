# https://www.codewars.com/kata/5afd81d0de4c7f45f4000239

from math import prod
from itertools import combinations
def find_min_max_product(arr, k):
    if len(arr) >= k:
        products = [ prod(comb) for comb in combinations(arr, k) ]
        return min(products), max(products)

