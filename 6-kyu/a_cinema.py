# https://www.codewars.com/kata/603301b3ef32ea001c3395d0

def cinema(b, g):
    x, y = sorted((b, g))
    d = y - x
    if y / x > 2:
        return None
    res  = 'YXY'* d + 'YX' * (x-d) 
    if b > g:
        return res.replace('X', 'G').replace('Y', 'B')
    else:
        return res.replace('X', 'B').replace('Y', 'G')
