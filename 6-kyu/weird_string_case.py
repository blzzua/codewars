# https://www.codewars.com/kata/52b757663a95b11b3d00062d

def to_weird_case(words):
    res = []
    parity = True
    for i, c in enumerate(words):
        parity = bool(1 + int(c == ' ') - parity)
        res.append(c.lower() if parity else c.upper())
    return ''.join(res)
