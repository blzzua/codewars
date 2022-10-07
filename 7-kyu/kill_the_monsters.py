# https://www.codewars.com/kata/5b36137991c74600f200001b

def kill_monsters(health, monsters, damage):
    hits = (monsters-1)//3
    health = health - hits*damage
    if health > 0:
        return f'hits: {hits}, damage: {hits * damage}, health: {health}'
    else:
        return f'hero died'


