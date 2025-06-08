# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

from itertools import cycle

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        key=self.key
        alphabet=self.alphabet
        res = []
        key_gen = cycle([alphabet.index(k) for k in key if k in alphabet])
        al_len = len(alphabet)
        for c in text:
            if c in alphabet:
                res.append(alphabet[(alphabet.index(c) + next(key_gen)) % al_len])
            else:
                next(key_gen)
                res.append(c)
        return ''.join(res)
    
    def decode(self, text):
        key=self.key
        alphabet=self.alphabet
        res = []
        key_gen = cycle([alphabet.index(k) for k in key if k in alphabet])
        al_len = len(alphabet)
        for c in text:
            if c in alphabet:
                res.append(alphabet[(alphabet.index(c) - next(key_gen)) % al_len])
            else:
                next(key_gen)
                res.append(c)
        return ''.join(res)
    
