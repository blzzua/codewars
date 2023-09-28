# https://www.codewars.com/kata/6512b3775bf8500baea77663

from string import ascii_letters as al
def gimme_the_letters(sp):
    a, sep, b  = sp.partition('-')
    return ''.join(c for c in al if a <= c <= b)
