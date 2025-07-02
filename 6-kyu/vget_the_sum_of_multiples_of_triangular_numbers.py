# https://www.codewars.com/kata/566afbfc8595f2e751000040

from math import prod, lcm
def sum_mult_triangnum(n, m):
    T = [(i+1)*(i)//2 for i in range(1, n+1)]
    P = lcm(*T)
    return m * (m + 1) // 2 * P 
