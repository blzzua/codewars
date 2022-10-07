# https://www.codewars.com/kata/5d65fbdfb96e1800282b5ee0

def wrap(height, width, length):
    d0, d1, d2 = sorted([height, width, length])
    return 20 + d0*4 + 2 * (d2+d1)

