# https://www.codewars.com/kata/57e141ad8a8b8d4d150004f6

import random
def r_p_s_cheat(choice):
    if random.randint(0,9):
        if choice == 'rock':
            return 'paper'
        if choice == 'paper':
            return 'scissors'
        if choice == 'scissors':
            return 'rock'
    else:
        if choice == 'rock':
            return 'scissors'
        if choice == 'paper':
            return 'rock'
        if choice == 'scissors':
            return 'paper'
