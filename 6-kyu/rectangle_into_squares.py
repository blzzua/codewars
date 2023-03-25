# https://www.codewars.com/kata/55466989aeecab5aac00003e

def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    res  = []
    square_remain = lng * wdth
    while square_remain > 0:
        a , b = sorted((lng, wdth))
        res.append(a)
        square_remain, lng, wdth = square_remain - a**2, a, b - a 
    return res
    
