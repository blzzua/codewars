# https://www.codewars.com/kata/56414fdc6488ee99db00002c

def absent_vowel(x): 
    for i, n in enumerate('aeiou'):
        if n not in x:
            return i

