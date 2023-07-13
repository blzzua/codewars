# https://www.codewars.com/kata/568ade64cfd7a55d9300003e

def calculator(distance, bus_drive, bus_walk):
    walk_time = distance / 5 * 60
    if walk_time > 120 :
        return 'Bus'
    mix_walk = (bus_walk / 5 * 60) + (bus_drive / 8 * 60)
    if mix_walk < walk_time and mix_walk != walk_time and walk_time >= 10:
        return 'Bus'
    else:
        return 'Walk'
