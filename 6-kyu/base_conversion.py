# https://www.codewars.com/kata/526a569ca578d7e6e300034e

def convert(input, source, target):
    ri = input[::-1]
    sbase = len(source)
    tbase = len(target)
    tlen = sum((sbase**i)*source.index(rc) for i, rc in enumerate(ri))
    res = ''
    while tlen:
        print(res, tlen)
        res += target[ tlen % tbase ]
        tlen //= tbase
    return res[::-1] or target[0]
