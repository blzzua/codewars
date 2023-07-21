# https://www.codewars.com/kata/589d1e88e8afb7a85e00004e

def number_increasing(n):
    i = n
    while True:
        if i == 1:
            return True
        if i < 1:
            return False
        if (i - 1) % 5 == 0:
            return True
        if i % 3 == 0:
            i = i // 3
        else:
            i = i - 5
