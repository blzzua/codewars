# https://www.codewars.com/kata/55ec55323c89fc5fbd000019

from string import ascii_lowercase as al
from itertools import count

def caesar_encode(phrase, init_shift):
    res = []
    for word, shift in zip(phrase.split(' '), count(init_shift)):
        shift = shift % 26
        res.append(word.translate(str.maketrans({k:v for k,v in zip(al, al[shift:] + al[:shift])})))
    return ' '.join(res)
