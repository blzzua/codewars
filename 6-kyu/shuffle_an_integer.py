# https://www.codewars.com/kata/6467a353f81b1f0031004eb8

import random
def shuffint(n):
    bits = list(bin(n)[2:])
    if all(b == '1' for b in bits):
        return 0
    random.shuffle(bits)
    res = int('0b' + ''.join(bits), 2)
    if res == n:
        # bad luck. try again.
        return shuffint(n)
    else:
        return res
