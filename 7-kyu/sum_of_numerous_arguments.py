# https://www.codewars.com/kata/55c5b03f8c28da9a51000045

def find_sum(*arg):
    if any(a < 0 for a in arg): 
        return -1
    else:
        return sum(arg)

