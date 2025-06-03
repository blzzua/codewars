# https://www.codewars.com/kata/556e0fccc392c527f20000c5

def xbonacci(signature, n):
    if n <= len(signature):
        return signature[:n]
    res = signature[:]
    seq = signature[:]
    for i in range(n-len(signature)):
        next_xbonacci_number = sum(seq)
        seq.append(next_xbonacci_number)
        seq.pop(0)
        res.append(next_xbonacci_number)
    return res
