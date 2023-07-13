# https://www.codewars.com/kata/5a02037ac374cbab41000089

def get_animals_count(legs_number, heads_number, horns_number):
    c = horns_number // 2
    r = legs_number // 2 - c - heads_number
    ch = heads_number - c - r
    return {'cows':c, 'rabbits': r, 'chickens': ch}
