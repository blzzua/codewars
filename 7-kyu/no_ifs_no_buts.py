# https://www.codewars.com/kata/592915cc1fad49252f000006
# 
# Write a function that accepts two parameters (a and b) and says whether a is smaller than, bigger than, or equal to b.
# There's only one problem...
# You can't use if statements, and you can't use shorthands like (a < b)?true:false;
# in fact the word "if" and the character "?" are not allowed in the code. 


from math import copysign
def no_ifs_no_buts(a, b):
    return [f"{a} is equal to {b}", [f"{a} is greater than {b}", f"{a} is smaller than {b}"][a < b]][a != b]
    
    
# clever: create dict with True/False keys(depends on a,b), and .get(True)
def no_ifs_no_buts(a, b):
    return {
        a == b: str(a) + " is equal to " + str(b),
        a < b: str(a) + " is smaller than " + str(b),
        a > b: str(a) + " is greater than " + str(b),
    }[True]
