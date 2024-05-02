# https://www.codewars.com/kata/55e2de13b668981d3300003d

def differentiate(poly):
    astr, x ,nstr =  poly.partition('x')
    if x == '':
        return "0"
    if astr == '-':
        a = -1
    elif astr == '':
        a = 1
    else:
        a = int(astr)
    if nstr == '':
        n = 1
    elif nstr.startswith('^'):
        n = int(nstr[1:])
        
    if n == 1:
        diffpower=''
        x = ''
    elif n == 2:
        diffpower=''
        x = 'x'
    else:
        diffpower='^' + str(n-1)
        x = 'x'
    return str (a * n) + x + diffpower

