# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69

def hamming(a,b):
    return sum(a!=b for a,b in zip(a,b) )
