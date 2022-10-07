# https://www.codewars.com/kata/588e2a1ad1140d31cb00008c

from itertools import combinations_with_replacement
def generate_pairs(m, n):
    return [*combinations_with_replacement(range(m,n+1),2)]

