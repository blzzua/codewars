# https://www.codewars.com/kata/5c4cb8fc3cf185147a5bdd02

from math import prod
def sum_or_product(a, n):
    a.sort()
    s = sum(a[-n:])
    p = prod(a[:n])
    return { s<p: 'product', s>p: 'sum', s==p: 'same'}[True]

