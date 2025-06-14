# https://www.codewars.com/kata/5ad1e412cc2be1dbfb000016

from string import ascii_uppercase

def insert_missing_letters(st):
    al = list(ascii_uppercase)
    res = []
    seen = set()
    for ch in st:
        res.append(ch)
        if ch not in seen:
            mis_index = (al.index(ch.upper()) + 1) % len(al)
            if mis_index:
                res.extend([letter for letter in al[mis_index:] if letter.lower() not in st])
        seen.add(ch)
    return ''.join(res)

