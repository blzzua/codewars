# https://www.codewars.com/kata/57eead3b5f79f6d977001fb7

def digit_all(x):
    if not isinstance(x, str):
        return 'Invalid input !'
    return ''.join(filter(lambda c: c.isnumeric(), x))
