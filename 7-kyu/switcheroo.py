# https://www.codewars.com/kata/57f759bb664021a30300007d

def switcheroo(s):
    d = {'a': 'b', 'b': 'a'}
    return ''.join(d.get(c, c) for c in s)

