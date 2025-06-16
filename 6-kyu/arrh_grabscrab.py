# https://www.codewars.com/kata/52b305bec65ea40fe90007a7

def grabscrab(said, possible_words):
    said = sorted(said)
    res = []
    for word in possible_words:
        if said == sorted(word):
            res.append(word)
    return res
