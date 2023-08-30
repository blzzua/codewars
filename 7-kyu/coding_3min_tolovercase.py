# https://www.codewars.com/kata/5713b0253b510cd97f001148

from string import ascii_lowercase as al
def to_lover_case(string):
    res = [c if not c.isalpha() else 'LOVE'[al.index(c.lower())%4]
         for c in string]
    return ''.join(res)
  
