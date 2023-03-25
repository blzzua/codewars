# https://www.codewars.com/kata/53670c5867e9f2222f000225

def is_orthogonal(u, v): 
    return not bool(sum(x*y for x,y in zip(u, v)))
