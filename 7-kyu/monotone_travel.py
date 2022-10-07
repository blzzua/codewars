# https://www.codewars.com/kata/54466996990c921f90000d61

def is_monotone(heights):
    return all(a<=b for a,b in zip(heights, heights[1:]))

