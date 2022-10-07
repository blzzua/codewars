# https://www.codewars.com/kata/62a933d6d6deb7001093de16

def get_the_vowels(word):
    w = ['a', 'e', 'i', 'o', 'u']
    wc = 0
    s = 0
    for c in word:
        if w[wc] == c:
            wc += 1 
            s += 1
        if wc >= len(w):
            wc = 0
    return s
    

