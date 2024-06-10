# https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b

def split_integer(num, parts):
    res = [0] * parts
    while num > 0:
        part = num // parts
        num -= part
        parts -= 1
        res[parts] = part
    return res[::-1]


# this kata can me solved with heapq: 
from heapq import *
def split_integer(num, parts):
    k = [0] * parts
    for i in range(1, num+1):
        heapq.heapreplace(k, k[0] + 1)
    return sorted(k)

# clever divmod math:
def split_integer(num, parts):
    little_part_value, big_parts_count = divmod(num, parts)
    return (parts - bit_parts_count) * [little_part_value] + big_parts_count * [little_part_value + 1]
