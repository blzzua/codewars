# https://www.codewars.com/kata/55f3facb78a9fd5b26000036

from math import prod
def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False 
    
def check_root(string):
    #validate
    s = string.split(',')
    if not all(map(isint,s)) or len(s) != 4:
        return 'incorrect input'
    l = list(map(int,s))
    if sum(l) != sum(range(l[0], l[-1]+1)):
        return 'not consecutive'
    # calculate
    pr = prod(l)+1
    sq = pr**0.5
    if int(sq)**2 == pr:
        return f'{pr}, {int(sq)}'

