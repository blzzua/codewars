# https://www.codewars.com/kata/5b097da6c3323ac067000036

def solve(alice, bob):
    ac = bc = 0
    for a, b in zip(alice, bob):
        ac +=  a > b
        bc +=  b > a
    return {ac > bc: f'{ac}, {bc}: Alice made "Kurt" proud!',
            ac < bc: f'{ac}, {bc}: Bob made "Jeff" proud!',
            ac == bc: f'{ac}, {bc}: that looks like a "draw"! Rock on!'}[True]


