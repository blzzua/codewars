# https://www.codewars.com/kata/59859f435f5d18ede7000050

def word_to_bin(word):
    return [ bin(256+ord(c))[3:] for c in word ]

