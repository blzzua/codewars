# https://www.codewars.com/kata/629e4d5f24b98110a83b2d0d

def robber_encode(sentence):
    notvowel = 'bcdfghjklmnpqrstvwxyz'
    return ''.join([f"{c}{'O' if c == c.upper() else 'o'}{c}" if c.lower() in notvowel else c for c in sentence])

