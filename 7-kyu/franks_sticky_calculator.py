# https://www.codewars.com/kata/5900750cb7c6172207000054

from math import log10
def sticky_calc(operation, val1, val2):
    newval1 = round(val1) * 10 ** int(log10(val2) + 1) + round(val2)
    val2 = round(val2)
    if operation == '+':
        return newval1+val2
    elif operation == '-':
        return newval1-val2
    elif operation == '*':
        return newval1*val2
    elif operation == '/':
        return round(newval1/val2)
 
