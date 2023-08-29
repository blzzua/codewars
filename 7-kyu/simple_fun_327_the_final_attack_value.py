# https://www.codewars.com/kata/5951b409aea9beff3f0000c6

from math import gcd
def final_attack_value(x,monster_list):
    for m in monster_list:
        if x >= m:
            x += m
        else:
            x += gcd(m, x)
    return x
