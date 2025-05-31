# https://www.codewars.com/kata/5551dc71101b2cf599000023

from math import perm
def max_pizza(cuts):
    if cuts < 0:
        return -1
    return (cuts**2 + cuts)//2 + 1
