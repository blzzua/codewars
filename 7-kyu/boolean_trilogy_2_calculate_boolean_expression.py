# https://www.codewars.com/kata/5f8070c834659f00325b5313

from operator import and_, or_
from functools import reduce
def calculate(expr, values):
    or_arr = []
    for _or_part in expr.split(' | '):
        and_arr = []
        for letter in _or_part.split(' & '):
            and_arr.append(values.get(letter))
        or_arr.append(reduce(and_ ,and_arr ,1))
    return reduce(or_, or_arr,0)


# eval solution:
def calculate(expr, values):
    for c in values:
        expr = expr.replace(c, str(values.get(c)))
    return eval(expr)   # eval is too easy

# but! clever solution is:
calculate = eval
