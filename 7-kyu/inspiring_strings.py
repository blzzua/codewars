# https://www.codewars.com/kata/5939ab6eed348a945f0007b2

def longest_word(string_of_words):
    return max(string_of_words.split()[::-1], key=len)

