# https://www.codewars.com/kata/567d71b93f8a50f461000019

def crossover(c1, c2, i):
    return [f'{c1[:i]}{c2[i:]}', f'{c2[:i]}{c1[i:]}']

