# https://www.codewars.com/kata/55606aeebf1f0305f900006f

def to_binary(n):
    if n < 0: n += 2**32
    return str(bin(n))[2:]

