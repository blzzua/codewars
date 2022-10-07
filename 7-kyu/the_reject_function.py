# https://www.codewars.com/kata/52988f3f7edba9839c00037d

from itertools import filterfalse
def reject(seq, predicate): 
    return [*filterfalse(predicate,seq)]



