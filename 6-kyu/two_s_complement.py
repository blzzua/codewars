# https://www.codewars.com/kata/58d4785a2285e7795c00013b

def to_twos_complement(binary, bits):
    binary = binary.replace(" ","")
    if int(binary, 2) < 2**(bits-1):
        return int(binary, 2) 
    else:
        return int(binary, 2)-2**(bits)

def from_twos_complement(n, bits):
    if n < 0:
        n = 2**bits + n
    return bin(n)[2:].zfill(bits) 
