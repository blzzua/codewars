# https://www.codewars.com/kata/562dbaf65d4ab6685c0000ed

from collections import defaultdict, Counter

def hasher(word):
    return tuple(Counter(sorted(word)).items())

wmap = defaultdict(list)
for word in word_list:
    wmap[hasher(word)].append(word)
    
def unscramble(scramble):
    return wmap.get(hasher(scramble))
