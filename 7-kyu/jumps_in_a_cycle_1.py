# https://www.codewars.com/kata/63f844fee6be1f0017816ff1

from math import gcd 

def get_jumps(cycle_list, k):
    l = len(cycle_list)
    return l // gcd(l,k)

    # actual solution.
    i = 0
    res = []
    while True: 
        res.append(cycle_list[i])
        i = (i + k) % len(cycle_list)
        if i == 0:
            break
    return len(res)
