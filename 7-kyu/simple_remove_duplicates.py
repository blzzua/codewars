# https://www.codewars.com/kata/5ba38ba180824a86850000f7

from collections import OrderedDict
def solve(arr): 
    return list(OrderedDict({k: None for k in arr[::-1]}).keys())[::-1]

