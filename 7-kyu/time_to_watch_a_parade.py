# https://www.codewars.com/kata/560d41fd7e0b946ac700011c

def parade_time(groups, location, speed, pref):
    return [ (location+i+1) // speed for i, c in enumerate(groups) if c == pref]
