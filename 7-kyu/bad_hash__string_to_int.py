# https://www.codewars.com/kata/596d93bd9b6a5df4de000049

from itertools import pairwise
def string_hash(s):
    a = sum(map(ord, s))
    b = sum(ord(j)-ord(i) for i,j in pairwise(s))
    c = (a | b) & (~a<<2)
    d = c ^ (32 * (s.count(' ') + 1))
    return d

