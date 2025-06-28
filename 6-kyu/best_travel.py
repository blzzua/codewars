# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

from itertools import combinations
def choose_best_sum(t, k, ls):
    max_trip = 0
    for comb in combinations(ls, k):
        cur_trip  = sum(comb)
        if cur_trip <= t:
            if cur_trip > max_trip:
                max_trip = cur_trip
    if max_trip > 0:
        return max_trip

