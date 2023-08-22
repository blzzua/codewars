# https://www.codewars.com/kata/56ce2f90aa4ac7a4770019fa

def evenator(s):
    f = ''.join(filter(lambda x: x.isalnum() or x.isspace(), s))
    return ' '.join( (x + x[-1]) if len(x) % 2 else x for x in f.split())
