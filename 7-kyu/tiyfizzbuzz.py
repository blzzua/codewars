# https://www.codewars.com/kata/5889177bf148eddd150002cc

def tiy_fizz_buzz(string):
    res = ''
    for c in string:
        if c.lower() in 'aeiou':
            if c.isupper():
                res += 'Iron Yard'
            else:
                res += 'Yard'
        elif c.isalpha() and c.isupper():
            res += 'Iron'
        else:
            res += c
    return res

