# https://www.codewars.com/kata/5ffc226ce1666a002bf023d2

def solution(mtrx):
    return any([[c for c in line if c != ' '] == ['>', 'x'] for line in (mtrx)])
        

