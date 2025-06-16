# https://www.codewars.com/kata/5a959662373c2e761d000183

import itertools
def ticker(text, width, tick):
    tgen = itertools.cycle((' ' * width) + text)
    return ''.join(itertools.islice(tgen, tick, tick+width))
