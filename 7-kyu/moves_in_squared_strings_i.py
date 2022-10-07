# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25

def vert_mirror(strng):
    return '\n'.join(w[::-1] for w in strng.split('\n'))

def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])

def oper(fct, s):
    return fct(s)

