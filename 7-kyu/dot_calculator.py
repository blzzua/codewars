# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531

from operator import add, sub, mul, floordiv as div
def calculator(txt):
    ops = {'+': add, '-': sub, '*': mul, '//': div}
    x,op,y = txt.split(' ')
    x = len(x); y=len(y)
    return '.'*ops.get(op)(x,y)
    



