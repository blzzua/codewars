# https://www.codewars.com/kata/634d0f7c562caa0016debac5

from itertools import zip_longest
def is_defended(attackers, defenders):
    a_s, d_s = 0, 0
    for a, d in zip_longest(attackers, defenders, fillvalue=0):
        if a > d:
            a_s += 1
        elif a < d:
            d_s += 1
    if a_s > d_s:
        return False
    elif d_s > a_s:
        return True
    else:
        return sum(defenders) >= sum(attackers)
    
