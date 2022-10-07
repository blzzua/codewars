# https://www.codewars.com/kata/5810085c533d69f4980001cf

from operator import add, sub, mul, truediv

def calculator(x,y,op):
    ops = {'+': add, '-': sub, '*': mul, '/':truediv  }
    try:
        return float(ops.get(op)(x,y))
    except (TypeError, ValueError):
        return "unknown value"

