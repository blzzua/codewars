# https://www.codewars.com/kata/533c46b140aafec05b000d31
import re
   
def translate(sentence):
    res = []
    for word in sentence.split(' '):
        orig_word = word
        capitalize = True if word[0].isupper() else False
        if any(letter.isdigit() for letter in orig_word):
            pass
        elif word[0].lower() in ('a','e','i','o','u'):
            word = re.sub(r'(\w+)', r'\1way', word, count=1)
        elif all(vowel not in orig_word.lower() for vowel in ('a','e','i','o','u')):
            word = re.sub(r'(\w+)', r'\1ay', word, count=1)
        else:
            word = re.sub(r'([^aeiou]+)([aeiou]\w*)', r'\2\1ay', word, count=1)
        word = word.capitalize() if capitalize else word
        res.append(word)
    return ' '.join(res)
