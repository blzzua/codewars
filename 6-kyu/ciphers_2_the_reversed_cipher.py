# https://www.codewars.com/kata/59474c656ff02b21e20000fc

def encode(s):
    res = []
    for word in s.split():
        if len(word) > 1:
            res.append(word[::-1][1:] + word[::-1][0])
        elif word[::-1]:
            res.append(word[::-1][0])
        else:
            res.append('')
    return ' '.join(res)

