# https://www.codewars.com/kata/5acc3634c6fde760ec0001f7

def solve(nums, div):
    return [i+i % div for i in nums]

