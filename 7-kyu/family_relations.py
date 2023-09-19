# https://www.codewars.com/kata/5eaf798e739e39001218a2f4

def relations(family_list, target_pair):
    p = {d: m for m, d in family_list}
    a, b = target_pair

    if p.get(a) == b:
        return 'Mother'
    if p.get(b) == a:
        return 'Daughter'

    if p.get(p.get(a)) == b:
        return 'Grandmother'
    if p.get(p.get(b)) == a:
        return 'Granddaughter'

    if p.get(a) == p.get(b):
        return 'Sister'
    if p.get(p.get(a)) == p.get(p.get(b)):
        return 'Cousin'

    if p.get(a) == p.get(p.get(b)):
        return 'Niece'
    if p.get(p.get(a)) == p.get(b):
        return 'Aunt'
    
    return None
