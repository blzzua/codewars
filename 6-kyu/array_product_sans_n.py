# https://www.codewars.com/kata/5b3e609cd58499284100007a

from math import prod

def product_sans_n(nums):
    zero_count  = nums.count(0)
    
    if zero_count == 0:
        pprod = prod(nums)
        return [pprod//i for i in nums]

    if zero_count == 1:
        pprod = prod(i for i in nums if i != 0)
        return [pprod if i == 0 else 0 for i in nums]

    if zero_count > 1:
        return [0] * len(nums)
