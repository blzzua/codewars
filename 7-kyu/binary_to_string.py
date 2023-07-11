# https://www.codewars.com/kata/5ab3495595df9ec78f0000b4

def b2c(b):
    ''' Binary to char'''
    if b:
        return chr(int(b,2))
    else:
        return ''

def binary_to_string(binary):
    return ''.join(map(b2c,binary.split('0b')))
