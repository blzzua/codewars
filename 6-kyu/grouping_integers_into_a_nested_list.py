# https://www.codewars.com/kata/583fe48ca20cfc3a230009a1

from itertools import groupby
def group_ints(lst, key):
    return [list(items_gen) for group, items_gen in groupby(lst, key=lambda x: x>=key)]
