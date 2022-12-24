# https://www.codewars.com/kata/56abc5e63c91630882000057

def is_featured(val):
    return val%3 == 0 and val%2 == 1 and len(str(val)) == len(set(str(val)))

def next_numb(val):
    while True:
        val += 1
        if is_featured(val):
            return val
        if val > 9999999999:
            return 'There is no possible number that fulfills those requirements'
