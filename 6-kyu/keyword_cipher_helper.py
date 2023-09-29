# https://www.codewars.com/kata/535c1c80cdbf5011e600030f

class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.abc = abc
        self.crypt = ''
        for c in keyword + abc:
            if not (c in self.crypt):
                self.crypt = self.crypt + c

    def _code(self, word, enc=True):
        res =''
        c, a = (self.crypt, self.abc) if enc else (self.abc, self.crypt)
        for char in word:
            if char in a:
                i = a.index(char)
                res += c[i]
            else:
                res += char
        return res
                
    def encode(self, plain):
        return self._code(plain, True)

    def decode(self, ciphered):
        return self._code(ciphered, False)
    
