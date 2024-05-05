# https://www.codewars.com/kata/543ddf69386034670d000c7d

from math import pi
minute_angle = 2 * pi / 60
hour_angle = 2 * pi / 12

def hand_angle(hours, minutes):
    hours = hours % 12
    ma = minute_angle * minutes
    ha = hour_angle * (hours + minutes/60)
    res = abs(ma-ha)
    if res > pi:
        return 2 * pi - res
    else:
        return res 
