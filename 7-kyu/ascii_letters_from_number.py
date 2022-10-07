# https://www.codewars.com/kata/589ebcb9926baae92e000001

def convert(s):
    return ''.join([chr(int(a)*10 + int(b)) for a,b in zip(s[::2],s[1::2])])

