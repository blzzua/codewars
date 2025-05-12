# https://www.codewars.com/kata/5906bc3e59a2f7d14e000048

from statistics import median
def liquid_mixing(densities):
    res = []
    cur_barrels = []
    for b in densities:
        cur_barrels.append(b)
        res.append(median(cur_barrels))
    return res    

