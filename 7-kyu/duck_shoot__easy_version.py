# https://www.codewars.com/kata/57d27a0a26427672b900046f

def duck_shoot(ammo, aim, ducks):
    return ducks.replace('2', 'X', int(ammo * aim))

