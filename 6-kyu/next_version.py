# https://www.codewars.com/kata/56c0ca8c6d88fdb61b000f06

def next_version(version):
    move = 1
    res = []
    for ordinal, digit in enumerate(version.split('.')[::-1]):
        digit = int(digit) + move
        move, digit = divmod(digit, 10)
        res.append(digit)
    res[-1] = res[-1] + move*10
    return '.'.join(map(str, res[::-1]))
