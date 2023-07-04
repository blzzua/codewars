# https://www.codewars.com/kata/6402205dca1e64004b22b8de

def find_caterer(budget, people):
    if people == 0:
        return -1
    bp = budget // people
    return { (bp<15): -1,
             (bp>=15): 1,
             (bp>=20): 2,
             (people>60 and bp>=24): 3,
             (bp>=30): 3}[True]
