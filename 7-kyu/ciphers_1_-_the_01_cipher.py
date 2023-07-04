# https://www.codewars.com/kata/593f50f343030bd35e0000c6

from string import ascii_lowercase as al
ascii_lowercase = {c: str(i % 2) for i, c in enumerate(al)}

def encode_char(c):
    return ascii_lowercase.get(c,c)

def encode(s):
    return ''.join(map(encode_char, s.lower()))
