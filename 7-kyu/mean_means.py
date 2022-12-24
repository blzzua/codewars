# https://www.codewars.com/kata/57c6b44f58da9ea6c20003da

from math import prod
def geo_mean(nums, arith_mean):
    absent = (len(nums)+1) * arith_mean - sum(nums)
    nums.append(absent)
    return prod(nums) ** (1/len(nums))
