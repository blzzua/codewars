# https://www.codewars.com/kata/55afed09237df73343000042

def is_lucky(n):
    return sum(map(int,str(n))) % 9 == 0
