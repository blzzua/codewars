# https://www.codewars.com/kata/5583d268479559400d000064

def binary_to_string(binary):
    res = ''
    for byte in list(zip(*[iter(binary)] * 8)):
        bytevalue = sum(int(bit) * (2**power) for power, bit in enumerate(byte[::-1]))
        byte_char = chr(bytevalue)
        res += byte_char
    return res


# short
return ''.join(chr(int(binary[i:i+8],2)) for i in range(0,len(binary),8))
