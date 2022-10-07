# https://www.codewars.com/kata/57ad85bb7cb1f3ae7c000039

from functools import reduce
def numbers_with_digit_inside(x, d):
    nums = [i for i in range(1, x + 1) if str(d) in str(i)]
    return [len(nums), sum(nums), reduce(lambda x,y: x*y, nums) if nums else 0]

