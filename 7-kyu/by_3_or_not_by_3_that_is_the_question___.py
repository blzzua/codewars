# https://www.codewars.com/kata/59f7fc109f0e86d705000043

def divisible_by_three(st):
    return st in '369' if int(st) < 10 else divisible_by_three(str(sum(map(int,st))))


