# https://www.codewars.com/kata/59b0ab12cf3395ef68000081

def to12hourtime(timestring):
    hh = int(timestring[:2])
    mm = str(timestring[2:])
    if hh > 12:
        hh = hh - 12
        return f'{hh}:{mm} pm'
    elif hh == 12:
        return f'{hh}:{mm} pm'
    if hh == 0:
        hh = 12
    return f'{hh}:{mm} am'
