# https://www.codewars.com/kata/5680781b6b7c2be860000036

def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']

