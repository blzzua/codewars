# https://www.codewars.com/kata/599da159a30addffd00000af

def collision(x1, y1, r1, x2, y2, r2): 
    return ((x1-x2)**2 + (y1-y2)**2)**0.5 <= r1+r2

