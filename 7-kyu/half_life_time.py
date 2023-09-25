# https://www.codewars.com/kata/59f33b86a01431d5ae000032

from math import log2
def half_life(initial, remaining, time):
    return time/log2(initial/remaining)
