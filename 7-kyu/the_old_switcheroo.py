# https://www.codewars.com/kata/55d410c492e6ed767000004f

def vowel_2_index(string):
    return ''.join(str(i)  if c.lower() in 'aeiou' else c for i,c in enumerate(string,1))

