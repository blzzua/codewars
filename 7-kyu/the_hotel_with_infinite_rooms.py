# https://www.codewars.com/kata/5b9cf881d6b09fc9ee0002b1
from math import ceil
def group_size(S, D):
    skip_steps =  int(((4*S*S - 4*S + 8*D +1)**0.5 - 2*S + 1)/2) - 1
    D = D - (skip_steps* (skip_steps-1) // 2 + S * skip_steps)
    S = S + skip_steps

    # actual solution
    while S < D:
        D -= S
        S += 1
    return S
