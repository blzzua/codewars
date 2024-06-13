# https://www.codewars.com/kata/58409435258e102ae900030f

def parity_bit(binary):
    res = []
    for byte in binary.split():
        if byte.count('1') % 2 == 0:
            res.append(byte[:-1])
        else:
            res.append('error')
    return ' '.join(res)
