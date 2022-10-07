# https://www.codewars.com/kata/5d95b7644a336600271f52ba

import math
def crusoe(n, d, ang, dist_mult, ang_mult):   
    lat = d*math.cos(math.radians(ang))
    lon = d*math.sin(math.radians(ang))
    for i in range(n-1):
        d = d*dist_mult
        ang = ang*ang_mult
        lat += d*math.cos(math.radians(ang))
        lon += d*math.sin(math.radians(ang))
    return lat, lon

