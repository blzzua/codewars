# https://www.codewars.com/kata/56e9ac87c3e7d512bc001363

def ascii_encrypt(plaintext):
    return ''.join([chr(ord(c) + i) for i, c in enumerate(plaintext)])
    
def ascii_decrypt(encrypted):
    return ''.join([chr(ord(c) - i) for i, c in enumerate(encrypted)])

