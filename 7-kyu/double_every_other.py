# https://www.codewars.com/kata/5809c661f15835266900010a

def double_every_other(lst):
    return [c * 2 if i%2 else c for i, c in enumerate(lst)]

