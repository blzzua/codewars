# https://www.codewars.com/kata/534d0a229345375d520006a0

from math import log
def power_of_two(x):
    if x < 2:
        return bool(x)
    while x > 1:
        if x % 2 == 1:
            return False
        else:
            x = x // 2
    return True


