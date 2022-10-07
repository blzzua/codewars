# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0

def last(s):
    return sorted(s.split(), key=lambda w: w[-1])

