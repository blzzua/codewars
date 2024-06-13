# https://www.codewars.com/kata/5a1502db46d84395ab00008a
from gmpy2 import log, is_prime

def solve(x, y):
    res = 0
    for n in range(int(log(y)/log(3)) + 1):
        for m in range(int(log(y)/log(2)) + 1):
            p = 2**m * 3**n + 1
            if x <= p <= y:
                if is_prime(p):
                    res += 1
    return res

# actually here precalculated seq:
# stone_brige_primes = [2, 3, 5, 7, 13, 17, 19, 37, 73, 97, 109, 163, 193, 257, 433, 487, 577, 769, 1153, 1297, 1459, 2593, 2917, 3457, 3889, 10369, 12289, 17497, 18433, 39367, 52489, 65537, 139969, 147457, 209953, 331777, 472393, 629857, 746497, 786433, 839809, 995329, 1179649, 1492993]
