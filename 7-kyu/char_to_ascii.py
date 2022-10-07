# https://www.codewars.com/kata/55e9529cbdc3b29d8c000016

def char_to_ascii(s):
    if s:
        res = {c: ord(c) for c in set(s) if c.isalpha()}
        return res

