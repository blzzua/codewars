# https://www.codewars.com/kata/58925dcb71f43f30cd00005f

from itertools import permutations
def latest_clock(a, b, c, d):
    variants = []
    for a,b,c,d in permutations((a,b,c,d)):
        if f'{a}{b}' < '24' and  f'{c}{d}' < '60':
            variants.append(f'{a}{b}:{c}{d}')
    return max(variants)
