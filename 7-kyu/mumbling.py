# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    return '-'.join((c*i).capitalize() for i,c in enumerate(s, 1))

