# https://www.codewars.com/kata/5b360fcc9212cb0cf300001f

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
def hex_to_base64(hex: str) -> str:
    res = ''
    data = [a+b for a,b in zip(hex[::2], hex[1::2])]
    for batch in batched(data, 3):
        len_batch = len(batch)
        if len_batch < 3:
            batch = (list(batch) + ['00', '00'])[:3]
        byte_8 = [int(byte, 16) for byte in batch]

        byte_6 = [0,0,0,0]
        byte_6[0] = (byte_8[0] >> 2) & 63
        byte_6[1] = ((byte_8[0] << 4) & 63) | (byte_8[1] >> 4)
        byte_6[2] = ((byte_8[1] << 2) & 63) | (byte_8[2] >> 6)
        byte_6[3] = byte_8[2] & 63
        if len_batch < 3:
            byte_6.pop()
        if len_batch < 2:
            byte_6.pop()
        res += ''.join([base64_alphabet[byte] for byte in byte_6])

    pad_length = (len_batch % 3)
    if pad_length > 0:
        res = res + "=" * (3-pad_length)
        pass
    return res
