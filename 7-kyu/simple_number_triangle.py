# https://www.codewars.com/kata/5a906c895084d7ed740000c2
from math import prod
def solve(n):
    # (2n)! / n!(n+1)!
    nom = [*range(1,2*n+1)]
    denom = [*range(1,n+1)] + [*range(1,n+2)]
    for d in denom[::]:
        if d in nom:
            nom.remove(d)
            denom.remove(d)
    return prod(nom) // prod(denom)
