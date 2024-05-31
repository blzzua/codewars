# https://www.codewars.com/kata/589414918afa367b4800015c

from math import inf
def absolute_values_sum_minimization(lst):
    min_value=inf;  min_item = lst[0]
    for x in lst:
        s = sum([abs(i - x) for i in lst])
        if s < min_value:
            min_value = s
            min_item = x
    return min_item

# clever:
# from statistics import median_low as absolute_values_sum_minimization

# use property of sorted array:
# return lst[(len(lst)-1)//2]
