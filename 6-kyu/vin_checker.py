# https://www.codewars.com/kata/60a54750138eac0031eb98e1

def check_vin(number):
    letters = 'ABCDEFGHJKLMNPRSTUVWXYZ0123456789'
    numbers = '123456781234579234567890123456789'
    weights = [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]

    if type(number) is not str \
        or len(number) != 17 \
        or any(x not in letters for x in number):
        return False

    lamap = {l: int(n) for l, n in zip(list(letters), list(numbers))}
    s = sum(lamap.get(n)*w for n, w in zip(number, weights))
    return '0123456789X'[s % 11] == number[8]
