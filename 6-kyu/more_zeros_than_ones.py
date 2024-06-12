# https://www.codewars.com/kata/5d41e16d8bad42002208fe1a

def more_zeros(s):
    res = []
    for char in s:
        if bin(ord(char))[2:].count('1') < bin(ord(char))[2:].count('0'):
            if char not in res:
                res.append(char)
    return res
