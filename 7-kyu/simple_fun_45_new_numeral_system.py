# https://www.codewars.com/kata/5888445107a0d57711000032

from string import ascii_uppercase
def new_numeral_system(number):
    i = ascii_uppercase.index(number)
    return [f'{a} + {b}'for a,b in zip(ascii_uppercase[:], ascii_uppercase[:i+1][::-1]) if a <= b]
    
