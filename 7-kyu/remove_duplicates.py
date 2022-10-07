# https://www.codewars.com/kata/53e30ec0116393fe1a00060b

def unique(integers):
    res = []
    for i in integers:
        if not i in res:
            res.append(i)
    return res

