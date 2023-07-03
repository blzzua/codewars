# https://www.codewars.com/kata/55e6125ad777b540d9000042

def get_count(*args):
    res = {'vowels': 0, 'consonants': 0}
    if args and isinstance(args[0], str):
        words = args
        vowels_char = 'aeiou'
        consonants_char = 'bcdfghjklmnpqrstvwxyz'
        for c in str(words).lower():
            if c in vowels_char:
                res['vowels'] += 1
                continue 
            elif c in consonants_char:
                res['consonants'] += 1
    return res
  
