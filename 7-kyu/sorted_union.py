# https://www.codewars.com/kata/5729c30961cecadc4f001878

def unite_unique(*args):
    res = []
    for arr in args:
        for i in arr:
            if i not in res:
                res.append(i)
    return res

