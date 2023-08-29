# https://www.codewars.com/kata/594cd799c08247a55a000004

def is_john_lying(a,b,s):
    js = abs(a) + abs(b)
    if js > s: 
        return False
    return (s % 2 == 1  and js % 2 == 1) or (s % 2 == 0 and js % 2 == 0)
