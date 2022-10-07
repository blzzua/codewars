# https://www.codewars.com/kata/55d6a0e4ededb894be000005

from string import ascii_lowercase
def encode(string):
    string = string.lower()
    al = ' '+ascii_lowercase
    s = [str(al.index(c)) if c.isalpha() else c for c in string]
    return ''.join(s)

