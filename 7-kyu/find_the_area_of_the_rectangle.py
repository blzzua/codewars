# https://www.codewars.com/kata/580a0347430590220e000091

def area(d, l): 
    a2 = d*d - l*l
    if a2 <= 0:
        return 'Not a rectangle'
    return round(a2**0.5*l,2)
