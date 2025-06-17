# https://www.codewars.com/kata/5270f22f862516c686000161
from itertools import islice

def batched(iterable, n):
    """from itertools import batched"""
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch
        batched

base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def to_base_64(string):
    if len(string) % 3 == 0:
        padding = 0
    else:
        padding = 3 - len(string) % 3
    string = string + '\0' * padding

    res = []
    for triple in batched(string, 3):
        str24bit = ''.join(format(ord(c), '08b') for c in triple)
        for tup6bit in batched(str24bit, 6):
            str6bit = ''.join(tup6bit)
            res.append(base64_alphabet[int(str6bit,2)])
    if padding:
        for _ in range(padding):
            res.pop()
    return ''.join(res)
    
def from_base_64(string):
    res = []
    for quad in batched(string, 4):
        str24bit = ''.join(format(base64_alphabet.index(c), '06b') for c in quad)
        for tup_byte in batched(str24bit, 8):
            byte = ''.join(tup_byte)
            res.append(chr(int(byte,2)))
    return ''.join(res).strip('\0')
