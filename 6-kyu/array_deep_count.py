# https://www.codewars.com/kata/596f72bbe7cd7296d1000029

def deep_count(a):
    res = 0
    for i in a:
        res+= 1
        if isinstance(i, list):
            res+=deep_count(i)
    return res
