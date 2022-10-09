# https://www.codewars.com/kata/58846d50f54f021d90000012

def rounders(value):
    a = list(map(int, str(value)))
    prev = 0
    for i, f in enumerate(a[::-1]):
        f = f + prev
        prev = int(f >= 5)
    return f*(10**i)
