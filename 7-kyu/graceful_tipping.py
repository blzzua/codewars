# https://www.codewars.com/kata/5eb27d81077a7400171c6820

from math import ceil
def graceful_tipping(bill):
    bill = bill*1.15
    for i in range(8,0,-1):
        if bill // 10**i:
            tr = bool(bill // 10**i) * 10**i//2
            tips = ceil(bill/tr)*tr
            return tips
    return ceil(bill)
