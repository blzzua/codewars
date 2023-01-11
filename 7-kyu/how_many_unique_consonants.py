# https://www.codewars.com/kata/5a19226646d843de9000007d

from collections import Counter
def count_consonants(text):
    cntr = Counter(text.lower()) 
    return len([letter for letter in cntr if letter not in 'aeiou' and 'a' <= letter <= 'z' ])
