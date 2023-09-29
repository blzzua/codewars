# https://www.codewars.com/kata/588847702ffea657ba00001b

from string import ascii_lowercase as al

def cipher26(message):
    res = ''
    prevsum = 0
    for letter in message:
        i = al.index(letter)
        d = (i - prevsum) % 26
        res = res + al[d]
        prevsum = (prevsum + d) % 26
    return res
