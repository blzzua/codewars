# https://www.codewars.com/kata/59cf8bed1a68b75ffb000026

def solve(s):
    vowels = []; consonant = []
    for c in sorted(s):
        if c in 'aeiou':
            vowels.append(c)
        else:
            consonant.append(c)
            
    if len(vowels) >= len(consonant):
        long_group = vowels
        short_group = consonant
    else:
        long_group = consonant
        short_group = vowels
    res = []
    while short_group:
        res.append(long_group.pop(0))
        res.append(short_group.pop(0))
        
    if len(long_group) > 1:
        return 'failed'
    else:
        return ''.join(res+long_group)
