# https://www.codewars.com/kata/5a40c250c5e284a76400008c

def bouncing_ball(initial, proportion):
    bounce = 0
    while initial > 1:
        initial = initial * proportion
        bounce += 1
    return bounce

