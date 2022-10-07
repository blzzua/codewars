# https://www.codewars.com/kata/544e2c60908f2da03600022a

#math already imported, default degrees and radians methods disabled
def degrees(rad):
    deg = round(rad * 180 / math.pi,2)
    if deg.is_integer():
        deg = int(deg)
    return f'{deg}deg'

def radians(deg):
    rad = round(deg / 180 * math.pi,2)
    if rad.is_integer():
        rad = int(deg)
    return f'{rad}rad'

    
math.degrees=degrees
math.radians=radians

