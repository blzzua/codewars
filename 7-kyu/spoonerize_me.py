# https://www.codewars.com/kata/56b8903933dbe5831e000c76

def spoonerize(words):
    a, b = words.split()
    return f'{b[0]}{a[1:]} {a[0]}{b[1:]}'

