# https://www.codewars.com/kata/595519279be6c575b5000016

from string import ascii_uppercase
def battle(x, y):
    al = ' '+ascii_uppercase
    res1 = sum([al.index(a) for a in x]) 
    res2 = sum([al.index(a) for a in y]) 
    if res1>res2:
        return x
    elif res2>res1:
        return y
    else:
        return 'Tie!'
        


