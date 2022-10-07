# https://www.codewars.com/kata/5bd00c99dbc73908bb00057a

from string import ascii_lowercase
def alpha_seq(string):
    alph = {v:k for k,v in enumerate(ascii_lowercase,1)}
    return ','.join([ (char*alph[char]).capitalize() for char in sorted(list(string.lower()))])

