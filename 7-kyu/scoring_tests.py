# https://www.codewars.com/kata/55d2aee99f30dbbf8b000001

def score_test(tests, right, omit, wrong):
    res = 0
    for a in tests:
        match a:
            case 0: 
                res += right
            case 1: 
                res += omit
            case 2: 
                res -= wrong
    return res

