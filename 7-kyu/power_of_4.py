# https://www.codewars.com/kata/544d114f84e41094a9000439

from math import log
def powerof4(n):
    if type(n) == int and n > 0:
        return n == 4**round(log(n, 4))
    else:
        return False

