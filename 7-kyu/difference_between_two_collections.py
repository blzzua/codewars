# https://www.codewars.com/kata/594093784aafb857f0000122

def diff(a, b):
    A = set(a)
    B = set(b)
    return sorted(list(A.difference(b)) + list(B.difference(a)))
