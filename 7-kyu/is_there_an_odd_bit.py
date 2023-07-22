# https://www.codewars.com/kata/5d6f49d85e45290016bf4718

def any_odd(x):
    return bool(bin(x)[2::][::-1][1::2].count('1'))
