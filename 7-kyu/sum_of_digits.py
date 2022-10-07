# https://www.codewars.com/kata/59cf805aaeb28438fe00001c

def sum_of_digits(digits): 
    if digits is None:
        return ''
    digits = str(digits)
    return  ' + '.join(list(digits)) + ' = '+ str(sum([int(d) for d in digits]))



