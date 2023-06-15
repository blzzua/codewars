# https://www.codewars.com/kata/5c563cb78dac1951c2d60f01

from string import ascii_lowercase
def pass_the_door_man(word): 
    for a,b in zip(word, word[1:]):
        if a == b:
            return ascii_lowercase.index(a) * 3 + 3
    return 0
