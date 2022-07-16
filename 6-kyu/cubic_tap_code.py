# https://www.codewars.com/kata/62d1eb93e5994c003156b2ae

import itertools
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
decipher,cipher = {}, {}
for l,(c1,c2,c3) in zip(letters,itertools.product(range(1,4),range(1,4),range(1,4))):
    cipher[l], decipher[(c3,c2,c1)] = (c3,c2,c1), l

def encode(s):
    return ' '.join(['.' * cnt for cnt in itertools.chain.from_iterable([cipher[letter] for letter in s])])

def decode(string):
    cnts = [w.count('.') for w in string.split(' ')]
    return ''.join([decipher[tuple(cnts[off:off+3])] for off in range(0,len(cnts),3)])
