# https://www.codewars.com/kata/5b04be641839f1a0ab000151

def game(words):
    for i, w1, w2 in  zip(range(len(words)), words, words[1:]):
        if w1 == '':
            return words[:i]
        if w1[-1:] != w2[:1]:
            return words[:i+1]
    return words
