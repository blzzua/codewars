# https://www.codewars.com/kata/54729e48e1d2a369e00000d3

from string import ascii_lowercase as al
def caesar(msg, shift):
    return msg.translate(str.maketrans(al, al[shift:]+al[:shift]))

def decode(msg, contents):
    res = []
    for i in range(26):
        variant = caesar(msg, i)
        if contents in variant:
            res.append(variant)
    return res
