# https://www.codewars.com/kata/63f9ec524362170065e5c85b

import math
def bounce_count(h, w, v):
    g = 9.81
    t  = ( 2 * h / g ) ** 0.5
    dist = v * t
    return int(math.floor(dist / w ))
