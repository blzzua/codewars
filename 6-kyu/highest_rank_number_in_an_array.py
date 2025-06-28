# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004

from collections import Counter
def highest_rank(arr):
    c = Counter(arr)
    max_qt = c.most_common(1)[0][1]
    return max([num for num, qt in c.most_common() if qt == max_qt])

