# https://www.codewars.com/kata/5865a407b359c45982000036

from itertools import permutations
def slogan_maker(array):
    a = []
    for item in array:
        if item not in a:
            a.append(item)
    return [' '.join(comb) for comb in permutations(a)]
