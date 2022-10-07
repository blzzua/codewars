# https://www.codewars.com/kata/5be085e418bcfd260b000028

def num_key_strokes(text):
    return sum(1 if c in "1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ `" else 2 for c in text)

