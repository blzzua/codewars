# https://www.codewars.com/kata/5b1b27c8f60e99a467000041

from collections import Counter
def anagram_difference(w1, w2):
    return sum((Counter(w1) - Counter(w2)).values()) + sum((Counter(w2) - Counter(w1)).values())
