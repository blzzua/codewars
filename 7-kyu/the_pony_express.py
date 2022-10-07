# https://www.codewars.com/kata/5b18e9e06aefb52e1d0001e9

def riders(stations):
    d, r = 0, 1 
    for s1, s2 in zip(stations, stations[1:]):
        if (d := d + s1) + s2 > 100:
            r, d  = r + 1 , 0
    return r

