# https://www.codewars.com/kata/581e09652228a337c20001ac

def cube_volume(h, r):
    a = min( r * 2 ** 0.5, h )
    return round(a**3, 2)
