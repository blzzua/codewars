# https://www.codewars.com/kata/529872bdd0f550a06b00026e

from math import prod
def greatest_product(st):
    ints = list(map(int, st)) 
    p1, p2, p3, p4, p5 = ints[:5]
    max_ = prod((p1, p2, p3, p4, p5))
    for p in ints[5:]:
        p1, p2, p3, p4, p5  =  p2, p3, p4, p5, p
        pret = prod((p1, p2, p3, p4, p5))
        if  pret > max_:
            max_ = pret
    return max_
