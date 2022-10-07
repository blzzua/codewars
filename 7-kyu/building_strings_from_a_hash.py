# https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2

def solution(pairs):
    return ','.join(sorted([f'{c} = {pairs[c]}' for c in pairs]))


