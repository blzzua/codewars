# https://www.codewars.com/kata/586ec0b8d098206cce001141

def inverse_slice(items, a, b):
    return [i for i in items if i not in items[a:b]]

