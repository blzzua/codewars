# https://www.codewars.com/kata/59a3e2897ac7fd05f800005f

import re
def validate_bet(game, text):
    N, M = game
    serie = re.split(r'(?:,| )+', text)
    if len(serie) != N:
        return None
    res = []
    for num in serie:
        if not num.isdigit():
            return None
        if not (1 <= int(num) <= M):
            return None
        if int(num) in res:
            return None
        res.append(int(num))
        
    return sorted(res)
