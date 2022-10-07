# https://www.codewars.com/kata/596776fbb4f24d0d82000141

def f(x, **kv):
    v = [kv[k] for k in sorted(kv.keys())]
    return (v*2)[v.index(x)+1]
    

