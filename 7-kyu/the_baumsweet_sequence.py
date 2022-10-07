# https://www.codewars.com/kata/5d2659626c7aec0022cb8006

def baum_sweet():
    n = 0
    while True:
        if n and '0' in bin(n)[2:].replace('00', ''):
            yield 0
        else:
            yield 1
        n += 1


