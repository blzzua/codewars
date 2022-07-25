# https://www.codewars.com/kata/62d81c6361677d57d8ff86c9

from itertools import pairwise
import math
def jumping(arr):
    HP = 20 
    DMG_REDUCTION = {
        'D' : 0, #Dirt block
        'B' : 0.5, #Bed
        'H' : 0.8, #Hay block
        'W' : 1, #Water block
    }

    for step, (s1, s2) in enumerate(pairwise(arr),1):
        d1, ___ = s1.split()
        d2, blk = s2.split()
        dst = int(d1) - int(d2)
        dmg = max(0, (dst - 3.5) * (1 - DMG_REDUCTION.get(blk)))
        HP = math.ceil(HP-dmg)
        if HP <= 0:
            return f"died on {step}"
    else:
        return f"jumped to the end with {HP} remaining HP"
