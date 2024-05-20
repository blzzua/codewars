# https://www.codewars.com/kata/526d42b6526963598d0004db

from  string import ascii_uppercase as al
class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.encode_map = str.maketrans({k:v for k,v in zip(al, al[shift:] + al[:shift])})
        self.decode_map = str.maketrans({v:k for k,v in zip(al, al[shift:] + al[:shift])})

    def encode(self, st):
        return st.upper().translate(self.encode_map)
        
    def decode(self, st):
        return st.upper().translate(self.decode_map)
