# https://www.codewars.com/kata/55a12bb8f0fac1ba340000aa

def find_function(func,arr):
    for f in func:
        try:
            return [*filter(f,arr)]
        except:
            continue

