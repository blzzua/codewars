# https://www.codewars.com/kata/5d4dd5c9af0c4c0019247110

from math import sin, radians, inf
def find_time_to_break(bearing_A, bearing_B):
    halfnet = 40/2
    angle_between_bearings = abs(bearing_A - bearing_B)/2
    if sin(radians(angle_between_bearings)) == 0:
        return inf
    distance = halfnet / sin(radians(angle_between_bearings))
    time = round(distance * 60 / 90 , 2)
    return time
