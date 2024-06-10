# https://www.codewars.com/kata/592645498270ccd7950000b4

from itertools import groupby
def typist(s):
    """
    res = 0
    for k, gen in groupby(s, key=lambda l: str.isupper(l)):
        # almost every group we must switch capslock
        res += 1
        # and type same case letters
        res += len(''.join(gen))
    # almost every, except if first group started from lowercase
    if s[0].islower():
        res -= 1
    """
    return sum([1 + len(''.join(gen)) for k, gen in groupby(s, key=lambda l: str.isupper(l))]) - bool(s[0].islower())

# clever zip pairwise comparation padded with lowercases letter 'a':
sum(a.islower()^b.islower() for a, b in zip('a'+s, s)) + len(s)


