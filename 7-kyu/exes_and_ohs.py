# https://www.codewars.com/kata/55908aad6620c066bc00002a

from collections import Counter
def xo(s):
    r = Counter(s.upper())
    return r['X'] == r['O']

