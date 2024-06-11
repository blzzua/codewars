# https://www.codewars.com/kata/58039f8efca342e4f0000023

from string import ascii_lowercase as al
def changer(s):
    translate_map = dict(zip(al + al.upper(), al[1:] + al +  al[:1])) 
    for k, v in translate_map.items():
        if v.lower() in 'aeiou': translate_map[k] = v.upper()
        elif v.lower() in 'bcdfghjklmnpqrstvxyz': translate_map[k] = v.lower()
    return s.translate(str.maketrans(translate_map))

# precomputed rainbow solution
return s.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA'))
