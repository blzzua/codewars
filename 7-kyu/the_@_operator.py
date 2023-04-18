# https://www.codewars.com/kata/631f0c3a0b9cb0de6ded0529

from functools import reduce

def op(a, b):
    if any((a is None, b is None, b == 0)):
        return None
    return (a + b) + (a - b) + (a * b) + (a // b)


def evaluate(equation):
    return reduce(op, map(int,equation.split(' @ ')))

