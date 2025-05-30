# https://www.codewars.com/kata/51e056fe544cf36c410000fb

import re
from collections import Counter
def top_3_words(text):
    c = Counter(re.findall('[a-z\']+', text.lower()))
    res = []
    for w, cnt in c.most_common(3):
        if w.strip('\''):
            res.append(w)
    return res
  
