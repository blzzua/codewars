# https://www.codewars.com/kata/592e2446dc403b132d0000be

from math import prod
def maximum_product(arr):
    prods = {}
    for i in range(len(arr)):
        prods[i] = prod(arr[:i]+arr[i+1:])    
    values = [arr[x] for x in prods if prods[x] == max(list(prods.values()))]
    return min(values)

