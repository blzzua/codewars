# https://www.codewars.com/kata/587f0abdd8730aafd4000035

from itertools import permutations
from hashlib import sha256

def sha256_cracker(hash_: str, chars: str) -> str:
    for comb in permutations(chars):
        if sha256(''.join(comb).encode('utf8')).hexdigest() == hash_:
            return ''.join(comb)

