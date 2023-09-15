# https://www.codewars.com/kata/588431bb76933b84520000d3

def is_infinite_process(a, b):
    if a > b:
        return True
    else:
        return (b - a ) % 2
