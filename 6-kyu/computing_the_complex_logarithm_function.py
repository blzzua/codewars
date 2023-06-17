# https://www.codewars.com/kata/590ba2baf06c49595f0000a0

import cmath
def log(real, imag):
    if real == 0:
        return None
    z = cmath.log(complex(real,imag))
    return [z.real,  z.imag]
