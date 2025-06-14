# https://www.codewars.com/kata/59f3178e3640cef6d90000d5

from itertools import combinations_with_replacement

def find(arr,n):
    res = 0
    max_size = min((n//min(arr), len(arr))) +1
    for i in range(1, max_size):
        for comb in combinations_with_replacement(arr, i):
            if sum(comb) == n: 
                res += 1
    return res
  
