# https://www.codewars.com/kata/56a13035eb55c8436a000041

import math
def cup_volume(d1, d2, height):
    return round( (d1 ** 2 + d1 * d2 + d2** 2) * height * math.pi /12, 2 )
