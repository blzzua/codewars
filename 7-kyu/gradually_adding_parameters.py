# https://www.codewars.com/kata/555b73a81a6285b6ce000047

def add(*args):
    return sum( a*b for a,b in enumerate(args,1) )

