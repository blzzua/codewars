# https://www.codewars.com/kata/538948d4daea7dc4d200023f

def convert_bits(a, b):
    return  bin(a ^ b).count('1')

