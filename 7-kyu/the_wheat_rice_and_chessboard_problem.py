# https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7

def squares_needed(grains):
    x = 0
    while grains > 0:
        grains, x = grains // 2, x + 1
    return x
