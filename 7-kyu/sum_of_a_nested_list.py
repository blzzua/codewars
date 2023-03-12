# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018

def sum_nested(lst):
    s = 0
    for i in lst:
        if not isinstance(i, list):
            s += i
        elif isinstance(i, list):
            s += sum_nested(i)
    return s
