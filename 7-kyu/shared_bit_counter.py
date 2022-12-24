# https://www.codewars.com/kata/58a5aeb893b79949eb0000f1

def shared_bits(a, b):
    return (a & b).bit_count() > 1 
