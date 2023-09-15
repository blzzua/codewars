# https://www.codewars.com/kata/5ae326342f8cbc72220000d2

def string_expansion(s):
    if not s: return s
    res = s[0] if s[0].isalpha() else ''
    rep = 1
    for digit, letter in zip(s,s[1:]):
        if digit.isnumeric():
            rep = int(digit) 
        if letter.isalpha():
            res += letter * rep
    return res
