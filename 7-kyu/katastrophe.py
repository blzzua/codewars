# https://www.codewars.com/kata/55a3cb91d1c9ecaa2900001b

from math import prod

def strong_enough( earthquake, age ):
    eq = prod(sum(line) for line in earthquake)
    remain = 1000 * (0.99 ** age)
    if remain >= eq:
        return 'Safe!'
    else:
        return 'Needs Reinforcement!'
