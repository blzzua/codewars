# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

from string import ascii_letters as al
def find_missing_letter(chars):
    return next(a for a, c  in zip(al[al.index(chars[0]):],chars) if a != c)
