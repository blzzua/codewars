# https://www.codewars.com/kata/56459c0df289d97bd7000083

from math import copysign
def generator(f,t,s):
    print(f,t,s)
    if s:
        s0 = int(copysign(s,t-f))
        s1 = int(copysign(1,t-f))
        return [*range(f,t+s1,s0)]
    else:
        return []

