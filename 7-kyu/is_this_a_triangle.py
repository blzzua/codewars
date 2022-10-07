# https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(*t):
    return all(sum(t)-l>l for l in t)


