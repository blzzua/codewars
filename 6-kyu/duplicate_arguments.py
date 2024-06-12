# https://www.codewars.com/kata/520d9c27e9940532eb00018e

def solution(*args):
    print(args)
    seen = set()
    for arg in args:
        if arg in seen:
            return True
        else:
            seen.add(arg)
    return False
