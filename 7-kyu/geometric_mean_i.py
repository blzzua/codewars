# https://www.codewars.com/kata/56ebcea1b9d927f9bf000544

"""
thank for discuss 
Output: the geometric mean from an array of numbers
1. consider negative numbers and strings in the array as invalid
2. output 0 instead when there are too many invalids in the array. Tolerance of 1 if the array has fewer than 10 entries, and tolerance of 10% if the array has greater than 10 entries.
"""

from math import prod
def geometric_meanI(arr):
    
    invalid_cnt = 0
    for i in arr:
        if isinstance(i, str) or i < 0:
            invalid_cnt +=1
    if (len(arr) < 10 and invalid_cnt > 1) or (len(arr)>=10 and invalid_cnt * 10 > len(arr)):
        return 0
    
    arr = [int(i) for i in arr if isinstance(i, int) and int(i)>=0]
    P = prod(arr)
    if P < 0: return 0
    return P**(1/len(arr))
