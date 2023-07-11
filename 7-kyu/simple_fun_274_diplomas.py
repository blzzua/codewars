# https://www.codewars.com/kata/591592b0f05d9a3019000087

from math import isqrt

def diplomas(h, w, n):
    sq = isqrt(h * w * n)
    while True:
        if (sq // h) * (sq // w) >= n:
            return sq
        sq += 1
