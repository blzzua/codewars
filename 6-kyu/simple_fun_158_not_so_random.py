# https://www.codewars.com/kata/58ad2e9c0e3c08126000003f

def not_so_random(b, w):
    if b + w == 0:
        return "Unsure"
    if b % 2:
        return "Black"
    else:
        return "White"
