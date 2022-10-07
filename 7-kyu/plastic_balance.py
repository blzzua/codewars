# https://www.codewars.com/kata/625ea5c1a071210065c923af

def plastic_balance(lst):
    while lst:
        if lst[0]+lst[-1] == sum(lst[1:-1]):
            return lst
        lst.pop(0)
        if lst:
            lst.pop(-1)
    return []

