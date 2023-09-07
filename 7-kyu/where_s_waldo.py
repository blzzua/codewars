# https://www.codewars.com/kata/638244fb08da6c61361d2c40

from collections import Counter
def find_waldo(crowd):
    """ Waldo is unique letter, except of birds over waterline"""
    is_sky = False
    waterline = 0
    people = []
    for i, line in enumerate(crowd[::-1]):
        if not is_sky and '~' in line: 
            is_sky = True
        for j, c in enumerate(line):
            if not is_sky:
                people.append(c)

    cnt = Counter(people)
    waldo = [l for l in cnt if cnt[l] == 1]
    if len(waldo) == 1:
        waldo = waldo[0]
        for i, line in enumerate(crowd):
            for j, c in enumerate(line):
                if c == waldo:
                    return [i, j]
    else: 
        return [0,0]

