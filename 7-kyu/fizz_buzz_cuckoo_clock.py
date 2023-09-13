# https://www.codewars.com/kata/58485a43d750d23bad0000e6

def fizz_buzz_cuckoo_clock(time):
    hh, mm = map(int,time. split(':'))
    if hh >= 13:
        hh = hh - 12
    if hh == 0:
        hh = 12
    if mm == 0:
        return ' '.join(hh * ['Cuckoo'])
    if mm == 30:
        return 'Cuckoo'
    res = []
    if mm % 3 == 0:
        res.append('Fizz')
    if mm % 5 == 0:
        res.append('Buzz')
    if res:
        return ' '.join(res)
    else:
        return 'tick'
