# https://www.codewars.com/kata/56e195d02bb22479e50016af

from gmpy2 import is_prime
def pernicious(n):
    if n < 2:
        return "No pernicious numbers"
    n = int(n)
    bits_count = {i: bin(i)[2:].count('1') for i in range(1,-~n)}
    res = [k for k,v in bits_count.items() if is_prime(v)]
    if res:
        return res
    else:
        return "No pernicious numbers"


