# https://www.codewars.com/kata/56cac350145912e68b0006f0

def arrange(strng):
    words = strng.split()
    for i, _ in enumerate(words[1:],1):
        if (i % 2 == 0 and len(words[i]) > len(words[i - 1])) or (i % 2 != 0 and len(words[i]) < len(words[i - 1])):
            words[i], words[i - 1] = words[i - 1], words[i]
    for i, word in enumerate(words):
        if i % 2 == 1:
            words[i] = word.upper() 
        else:
            words[i] = word.lower() 
    return ' '.join(words)
