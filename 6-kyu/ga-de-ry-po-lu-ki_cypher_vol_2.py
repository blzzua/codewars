# https://www.codewars.com/kata/592b7b16281da94068000107

def encode(message, key_):
    tr_map = {}
    for k1, k2 in  zip(key_[::2],  key_[1::2]):
        tr_map[k1.upper()]=k2.upper()
        tr_map[k1.lower()]=k2.lower()
        tr_map[k2.upper()]=k1.upper()
        tr_map[k2.lower()]=k1.lower()
    return message.translate(str.maketrans(tr_map))

decode = encode
