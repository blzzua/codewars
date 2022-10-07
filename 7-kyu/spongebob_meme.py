# https://www.codewars.com/kata/5982619d2671576e90000017

def sponge_meme(s):
    return ''.join([c.lower() if i%2 else c.upper() for i,c in enumerate(s)])

