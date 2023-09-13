# https://www.codewars.com/kata/5a9e86705ee396d6be000091

from collections import Counter
def check_three_and_two(array):
    c = Counter(array)
    return 2 in c.values() and 3 in c.values()
