# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

from collections import Counter
def duplicate_encode(word):
    c = Counter(word.lower())
    return ''.join('(' if c[ch] == 1 else ')' for ch in word.lower())
