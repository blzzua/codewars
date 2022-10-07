# https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1

def bin_rota(arr):
    ret = list()
    rev = 0
    for line in arr:
        if rev:
            line = line[::-1]
        rev = 1 - rev
        ret = ret + line
    return ret

        

