# https://www.codewars.com/kata/5797bbb34be9127074000132

def tetration(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    r = x
    for i in range(y-1):
        r = pow(x,r)
    return r

