# https://www.codewars.com/kata/58558673b6b0e5a16b000028

def fight_resolve(defender, attacker): 
    if (defender.lower() == defender) == (attacker.lower() == attacker):
        return -1
    defender_win = { 'a': 's', 'k':'a', 'p': 'k', 's': 'p'}
    a = attacker.lower()
    d = defender.lower()
    if defender_win[d] == a:
        return defender
    else:
        return attacker
