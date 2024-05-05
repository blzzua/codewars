# https://www.codewars.com/kata/582406166cf35b7f93000057

from itertools import permutations
def check_date(y,m,d):
    datestring = f'{y:02d}/{m:02d}/{d:02d}'
    if m in (1,3,5,7,8,10,12) and 1 <= d <= 31:
        return datestring 
    if m in (4,6,9,11) and 1 <= d <= 30:
        return datestring
    if m == 2 and 1 <= d <= 28:
        return datestring
    if m == 2 and d == 29 and y % 4 == 0:
        return datestring
    return False    
        
def unique_date(x, y, z):
    res = [check_date(a,b,c) for a, b, c in permutations((x,y,z))]
    correct_answers = [s for s in res if s]
    uniq_anwers = list(set(correct_answers))
    if len(uniq_anwers) == 0:
        return 'invalid'
    if len(uniq_anwers) == 1:
        return uniq_anwers[0]
    if len(uniq_anwers) > 1:
        return 'ambiguous'
