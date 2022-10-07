# https://www.codewars.com/kata/558aa460dcfb4a94c40001d7

def mpg2lp100km(mpg):
    return round(3.785411784/((mpg * 1.609344)/100), 2)
    
def lp100km2mpg(lp100km):
    return round((100/1.609344) / (lp100km /3.785411784), 2)

