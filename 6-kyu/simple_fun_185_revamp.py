# https://www.codewars.com/kata/58bcfe1e23fee9fd95000007

def revamp(string):
    words = [''.join(sorted(word)) for word in string.split()]
    return ' '.join(sorted(words, key=lambda word: (sum(map(ord, word)), len(word), word)))
