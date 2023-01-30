# https://www.codewars.com/kata/546ba103f0cf8f7982000df4

from operator import mul,add,sub
ops = {'add': add, 'subtract': sub, 'multiply': mul}

def calculate(n1, n2, o):
    db = lambda x: int(x,2)
    res = ops.get(o)(*map(db, (n1, n2)))
    return '{:b}'.format(res)
