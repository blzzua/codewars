# https://www.codewars.com/kata/567b39b27d0a4606a5000057

from random import random
def mutate(chromosome, p):
    flip = {'1': '0','0': '1'}
    return ''.join(flip[c] if p > random() else c for c in chromosome)
    

