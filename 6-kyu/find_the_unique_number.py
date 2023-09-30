# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

from collections import Counter
def find_uniq(arr):
    return Counter(arr).most_common(2)[-1][0]
