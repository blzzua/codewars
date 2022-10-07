# https://www.codewars.com/kata/5892595f190ca40ad0000095

from itertools import zip_longest as zip
def mispelled(word1,word2):
    return (word1 in word2 and len(word1) == len(word2)-1 or word2 in word1 and len(word2) == len(word1)-1)\
           or sum(a != b for a,b in zip(word1,word2)) <= 1 

