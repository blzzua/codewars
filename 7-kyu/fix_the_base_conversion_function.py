# https://www.codewars.com/kata/57cded7cf5f4ef768800003c

#fix the function below!

def convert_num(number, base):
    try:
        if base == 'hex':
            return hex(number)
        if base == 'bin':
            return bin(number)
        return 'Invalid base input'
    except TypeError:
        return 'Invalid number input'


