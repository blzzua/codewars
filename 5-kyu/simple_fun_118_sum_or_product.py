# https://www.codewars.com/kata/589d581680458f695200008e

from math import prod
def sum_or_product(arr):
    print(arr)
    rest = [a for a in arr if a not in (1,2)]
    c1 = arr.count(1) 
    c2 = arr.count(2)
    if c1 > c2:
        rest += [3] * ((c1  - c2) // 3 + c2)
        one_or_two = (c1  - c2 ) % 3
    else:
        rest += [3] * c1 + [2] * (c2 - c1)
        one_or_two = 0
    if rest:
        min_element_index = rest.index(min(rest))
        if one_or_two == 2:
            rest[min_element_index] *= one_or_two
        elif one_or_two == 1: 
            rest[min_element_index] += one_or_two
    else:
        rest = [one_or_two]
    return prod(rest)

