# https://www.codewars.com/kata/62204bb40e88a5004a662265

from math import lcm
def how_many(m, x):
    if m <= 0: 
        return 0
    a, op, b = x.split(' ')
    a, b = int(a), int(b)
    ab_lcm = lcm(a,b)
    if op == 'and':
        return m//ab_lcm
    elif op == 'or':
        return m//a + m//b - m//ab_lcm
