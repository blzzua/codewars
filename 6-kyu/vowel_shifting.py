# https://www.codewars.com/kata/577e277c9fb2a5511c00001d

def vowel_shift(text,n):
    if not text:
        return text
        
    vowels = {i: c for i, c in enumerate(text) if  c.lower() in ['a','e','i','o','u']}
    if len(vowels) == 0:
        return text

    shift = -(n % len(vowels))
    vowels_shifted = list(vowels.values())[shift:] + list(vowels.values())[:shift]
    replace_map = dict(zip(vowels.keys(), vowels_shifted))
    return ''.join(replace_map.get(i,c) for i, c in enumerate(text))
