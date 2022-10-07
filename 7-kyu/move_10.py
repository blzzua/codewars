# https://www.codewars.com/kata/57cf50a7eca2603de0000090

from string import ascii_lowercase as l
def move_ten(st):
    ll = l+l
    return ''.join(map(lambda c: ll[l.index(c)+10], st))

