# https://www.codewars.com/kata/58670300f04e7449290000e5

def longest(words):
    return len(max(words, key=len))

