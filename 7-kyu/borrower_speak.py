# https://www.codewars.com/kata/57d2ba8095497e484e00002e

def borrow(s):
    return ''.join(c.lower() for c in s if c.isalpha())
