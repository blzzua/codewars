# https://www.codewars.com/kata/5a0178f66f793bc5b0001728

from collections import Counter
from string import ascii_lowercase, digits

def longest_palindrome(s):
    c = Counter([letter for letter in s.lower() if letter in ascii_lowercase + digits])
    res = 0
    for letter, cnt in c.items():
        if cnt >= 2:
            res += (cnt // 2  * 2)
            c[letter] -= (cnt // 2  * 2)
    if sum(c.values()): #  > 0
        return res+1
    else:
        return res
