# https://www.codewars.com/kata/56ed20a2c4e5d69155000301

def scale(strng, k, v):
    res = ''
    lines = strng.split('\n')
    for sub in lines:
        t = ''
        for c in sub:
            t += c*k
        res += (t+'\n')*v
        t = ''
    return res.strip('\n')

