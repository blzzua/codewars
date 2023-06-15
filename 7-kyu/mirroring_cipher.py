# https://www.codewars.com/kata/571af500196bb01cc70014fa

from string import ascii_lowercase

def mirror(code, key=ascii_lowercase):
    trans = str.maketrans(key, key[::-1])
    return code.lower().translate(trans)
