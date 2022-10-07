# https://www.codewars.com/kata/5660aa3d5e011dfd6e000063

def find_spaceship(astromap):
    for i, row in enumerate(reversed(astromap.split('\n'))):
        for j, cell in enumerate(row):
            if cell == 'X':
                return [j,i]
    else:
        return 'Spaceship lost forever.'

