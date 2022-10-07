# https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74

def zombie_shootout(zombies, distance, ammo):
    distance = distance * 2
    if distance > ammo and zombies > ammo:
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."    
    if zombies > distance: 
        return f"You shot {distance} zombies before being eaten: overwhelmed."
    return f"You shot all {zombies} zombies."

