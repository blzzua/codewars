# https://www.codewars.com/kata/59564f3bcc15b5591a00004a

def filter_even_length_words(words):
    return [word for word in words if len(word) % 2 == 0]
