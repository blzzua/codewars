# https://www.codewars.com/kata/5877e7d568909e5ff90017e6

import itertools 

def find_all(sum_dig, digs):
    allowed_numbers = [comb for comb in itertools.combinations_with_replacement(range(1,10), digs) if sum(comb) == sum_dig]
    if allowed_numbers:
        prep = lambda nums: int(''.join(map(str, nums)))
        return [len(allowed_numbers), prep(min(allowed_numbers)), prep(max(allowed_numbers))]
    else:
        return []

#
# https://oeis.org/A009994
