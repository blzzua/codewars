# https://www.codewars.com/kata/59c8b38423dacc7d95000008

def isValid(formula):
    return False if 1 in formula and 2 in formula or 3 in formula and 4 in formula or 5 in formula and not 6 in formula or 5 not in formula and 6 in formula or 7 not in formula and 8 not in formula else True
        

