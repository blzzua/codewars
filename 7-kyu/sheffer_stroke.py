# https://www.codewars.com/kata/5d82344d687f21002c71296e

def NOT(a):
    return sheffer(a,a)

def AND(a, b):
    return sheffer(sheffer(a,b), sheffer(a,b))


def OR(a, b):
    return sheffer(sheffer(a,a), sheffer(b,b))
