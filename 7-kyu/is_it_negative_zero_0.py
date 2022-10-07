# https://www.codewars.com/kata/5c5086287bc6600001c7589a

import math
def is_negative_zero(n):
    return n == -0.0 and math.copysign(1, -n) == 1


