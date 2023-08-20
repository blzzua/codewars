# https://www.codewars.com/kata/6473603854720900496e1c82

def step(x, y):
    x, y = sorted((x,y))
    if x == y:
        return 0
    dd = y - x - 1
    s = int(dd**0.5)
    if s*s + s > dd:
        return 2 * s 
    else:
        return 2 * s  + 1
