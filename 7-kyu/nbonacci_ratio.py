# https://www.codewars.com/kata/5e60cc55d8e2eb000fe57a1c

def n_bonacci_ratio(n):
    fnp = 0
    fn = 1
    for i in range(25):
        fnp, fn = fn, n*fn + fnp
    return fn/fnp


