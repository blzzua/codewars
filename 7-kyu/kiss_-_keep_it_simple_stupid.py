# https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1

def is_kiss(words):
    w = words.split()
    if max(map(len, w)) <= len(w):
        return 'Good work Joe!'
    else:
        return 'Keep It Simple Stupid'
