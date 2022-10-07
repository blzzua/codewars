# https://www.codewars.com/kata/5831c204a31721e2ae000294

def swap(st):
    return ''.join( c.upper() if c in 'aeiou' else c for c in st)

