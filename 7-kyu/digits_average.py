# https://www.codewars.com/kata/5a32526ae1ce0ec0f10000b2

from math import ceil
def digits_average(input):
    if input > 9:
        return digits_average(int(''.join([str(ceil((int(a) + int(b)) / 2)) for a,b in zip(str(input), str(input)[1:])])))
    else:
        return input
