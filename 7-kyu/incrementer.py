# https://www.codewars.com/kata/590e03aef55cab099a0002e8

def incrementer(nums):
    return [ (n+i) %10 for i, n in enumerate(nums,1)]

