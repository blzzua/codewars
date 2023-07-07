# https://www.codewars.com/kata/588e0f11b7b4a5b373000041

def lowest_temp(t):
    return min(map(int,t.split()),default=None)
