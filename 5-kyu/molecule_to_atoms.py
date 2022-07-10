# https://www.codewars.com/kata/52f831fa9d332c6591000511
import collections
import re
def parse_molecule (formula):
    #print(formula)
    for r in r'\(([^\)]+)\)(\d+)', r'\[([^\]]+)\](\d+)', r'\{([^\}]+)\}(\d+)', r'([A-Z][a-z]?)(\d+)':
        formula = re.sub(r, lambda pair: ''.join(pair.group(1) for _ in range(int(pair.group(2)))), formula)
    ravel = re.findall(r'[A-Z][a-z]?', formula)
    #print(ravel)
    ret = collections.Counter(ravel)
    return dict(ret)
