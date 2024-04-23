# https://www.codewars.com/kata/573c84bf0addf9568d001299

def yes_no(arr):
    res = []
    stopsize = len(arr) 
    a = arr[:]
    i = 0
    while len(res) < stopsize:
        if i < len(a)-1:
            res.append(a.pop(i))
            a.append(a.pop(i))
            i = i % len(a)
        else:
            res += a
    return res
