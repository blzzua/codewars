# https://www.codewars.com/kata/56dc695b2a4504b95000004e

from string import ascii_lowercase
def caeser(message, key):
    alpha = ' '+ascii_lowercase+ascii_lowercase
    return ''.join(alpha[(alpha.index(c) + key)] if c in ascii_lowercase else c for c in message.lower()).upper()
    

