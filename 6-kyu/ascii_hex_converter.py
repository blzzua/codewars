# https://www.codewars.com/kata/52fea6fd158f0576b8000089

class Converter():
    @staticmethod
    def to_ascii(h):
        #return ''.join(chr(int(a+b,16)) for a,b in itertools.batched(h,2)) # itertools.batched implemented only from python 3.12 
        return ''.join(chr(int(a+b,16)) for a, b in zip(h[::2], h[1::2]))
        
    
    @staticmethod
    def to_hex(s):
        return ''.join(map(lambda c: '{:x}'.format(ord(c)), s))


# clever:
    def to_ascii(h):
        return bytes.fromhex(h).decode()
    
    def to_hex(s):
        return s.encode().hex()
