# https://www.codewars.com/kata/5519e930cd82ff8a9a000216

def hamming_weight(x):
    return sum((x>>i)%2 for i in range(32))

