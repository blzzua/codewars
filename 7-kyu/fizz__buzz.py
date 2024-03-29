# https://www.codewars.com/kata/51dda84f91f5b5608b0004cc

def solution(number):
    res = [0, 0, 0]
    for i in range(1, number):
        if i % 15 == 0:
            res[2] += 1
        elif i % 3 == 0:
            res[0] += 1
        elif i % 5 == 0:
            res[1] += 1
    return res

# clever math: [(number - 1) // 3 - (number - 1) // 15, (number - 1) // 5 - (number - 1) // 15, (number - 1) // 15]
