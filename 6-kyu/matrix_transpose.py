# https://www.codewars.com/kata/52fba2a9adcd10b34300094c

def transpose(matrix):
    return [list(col) for col in zip(*matrix)]
