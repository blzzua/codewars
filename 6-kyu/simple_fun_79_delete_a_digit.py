# https://www.codewars.com/kata/5894318275f2c75695000146

def delete_digit(n):
    res = 0
    for i in range(len(str(n))):
        var = int(str(n)[:i:] + str(n)[i+1::])
        if var > res:
            res = var
    return res
