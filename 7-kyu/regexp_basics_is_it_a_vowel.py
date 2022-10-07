# https://www.codewars.com/kata/567bed99ee3451292c000025

def is_vowel(s): 
    if len(s) == 1:
        return s.lower() in "aeiou"
    else:
        return False

