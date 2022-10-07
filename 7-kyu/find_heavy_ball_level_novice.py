# https://www.codewars.com/kata/544047f0cf362503e000036e

def find_ball(scales):
    l, r = [0,1,2,3], [4,5,6,7]

    w = scales.get_weight(l, r)
    res = l[:] if w == -1 else r[:]
    l, r = res[:2], res[2:]
    
    w = scales.get_weight(l, r)
    
    res = l[:]  if w == -1 else r[:]
    l, r =res[:1], res[1:]
    w = scales.get_weight(l, r)

    return res[0] if w == -1 else res[1]

