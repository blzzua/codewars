# https://www.codewars.com/kata/57d60363a65454701d000e11

from math import ceil
def cut_fruits(fruits):
    res = []
    for f in fruits:
        if f not in FRUIT_NAMES:
            res.append(f)
        else:
            l = len(f)
            cut = ceil(l / 2)
            f1 = f[:cut]
            f2 = f[cut:]
            res.extend([f1,f2])
    return res
