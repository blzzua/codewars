# https://www.codewars.com/kata/5a2e8c0955519e54bf0000bd

def check_digit(number, index1, index2, digit):
    s = str(number)
    i1, i2 = sorted( (index1, index2))
    return str(digit) in s[i1:i2+1]
