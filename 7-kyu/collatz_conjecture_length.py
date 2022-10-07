# https://www.codewars.com/kata/54fb963d3fe32351f2000102

def collatz(n):
    i = 1
    while n > 1:
        i += 1
        if n % 2:
            n = n * 3 + 1
        else:
            n = n // 2
    return i

