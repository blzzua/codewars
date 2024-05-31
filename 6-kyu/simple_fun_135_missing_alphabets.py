# https://www.codewars.com/kata/58a664bb586e986c940001d5

al = 'abcdefghijklmnopqrstuvwxyz'

def missing_alphabets(st):
    st = list(st)
    res = []
    while st:
        letter = st.pop(0)
        if letter not in res:
            res = res + list(al)
        res.pop(res.index(letter))
    return ''.join(sorted(res))
