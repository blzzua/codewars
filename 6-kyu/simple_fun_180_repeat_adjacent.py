# https://www.codewars.com/kata/58b8dccecf49e57a5a00000e

from itertools import groupby
def repeat_adjacent(string):
    groups= [len([*content])>1 for g, content in groupby(string)]
    bg = 0
    inbg = False
    for a,b in zip(groups, groups[1:]):
        if b and a:
            if not inbg: 
                bg += 1
                inbg = True
        if a and not b and inbg:
            inbg = False
    return bg
