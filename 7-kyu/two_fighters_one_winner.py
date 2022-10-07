# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b

def declare_winner(fighter1, fighter2, first_attacker):
    round = first_attacker
    while True:
        if round == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            round = fighter2.name

        elif round == fighter2.name:
            fighter1.health -= fighter2.damage_per_attack
            round = fighter1.name

        if fighter2.health <= 0:
            return fighter1.name
        if fighter1.health <= 0:
            return fighter2.name

