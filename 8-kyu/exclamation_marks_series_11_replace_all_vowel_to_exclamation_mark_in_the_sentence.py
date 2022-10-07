# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

def replace_exclamation(s):
    return ''.join(['!' if c.lower() in 'aeiou' else c for c in s])

