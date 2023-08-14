# https://www.codewars.com/kata/5a224a15ee1aaef6e100005a

def invert_triangle(t):
    return '\n'.join(l for l in t.translate(str.maketrans({' ': '#', '#': ' '})).split('\n')[::-1])
