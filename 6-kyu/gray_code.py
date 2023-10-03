# https://www.codewars.com/kata/5416ce834c2460b4d300042d

def bin2gray(bits):
    return [a^b for a, b in zip([0]+bits, bits)]
    
def gray2bin(bits):
    res = [bits[0]]
    [res.append(res[-1]^b) for b in bits[1:]]
    return res
