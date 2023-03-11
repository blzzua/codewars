# https://www.codewars.com/kata/563fb342f47611dae800003c

def trim(phrase, size):
    l = len(phrase)
    if l <= size:
        return phrase
    else:
        trim = size-3
        if l < 3 or trim <= 0:
            return phrase[:size] + '...'
        else:
            return phrase[:trim] + '...'
