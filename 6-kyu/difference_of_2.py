# https://www.codewars.com/kata/5340298112fa30e786000688

from itertools import combinations
def twos_difference(lst): 
    return [(a,b) for a,b in combinations(sorted(lst),2) if b - a == 2]
