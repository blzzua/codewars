# https://www.codewars.com/kata/55b95c76e08bd5eef100001e

def count_arara(n):
    res = []
    while n > 0:
        if n > 1:
            res.append()
            n -= 2
        else:
            res.append('anane')
            n -= 1
    return ' '.join(res)
