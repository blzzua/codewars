# https://www.codewars.com/kata/56f1c6034d0c330e4a001059

# from string import hexdigits ~ '0123456789abcdefABCDEF'

import random
def generate_color_rgb():
    return '#'+''.join(random.choice('0123456789abcdefABCDEF') for i in range(6))

# clever: f'#{random.randint(0,0xffffff):06x}'
