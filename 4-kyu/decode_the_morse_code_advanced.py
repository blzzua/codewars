# https://www.codewars.com/kata/54b72c16cd7f5154e9000457

from itertools import groupby

def decode_bits(bits):
    binseq = [''.join(data) for g, data in groupby(bits.strip('0'))]
    len_dot = min(len(char) for char in binseq)
    len_dash = 3 * len_dot
    res = []
    for char in binseq:
        if char[0] == '1':
            if len(char) < len_dash:
                res.append('.')
            else:
                res.append('-')
        elif len(char) > len_dot:
            if len(char) <= len_dash:
                res.append(' ')
            else:
                res.append('   ')
    return ''.join(res)

from preloaded import MORSE_CODE
MORSE_CODE['|']=' '
def decode_morse(morse_code):
    res = [MORSE_CODE.get(i,'') for i in morse_code.strip().replace('   ', ' | ').split()]
    return ''.join(res)
