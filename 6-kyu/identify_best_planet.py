# https://www.codewars.com/kata/6474b8964386b6795c143fd8

REQUIRED_ELEMENTS = 'H', 'C', 'N', 'O', 'P', 'Ca'
import re

def best_planet(solar_system, max_size):
    candidates = []
    for system in solar_system:
        elements = re.findall(r'[A-Z][a-z]?',system)
        if not all(req_el in elements for req_el in REQUIRED_ELEMENTS):
            continue
        size = int(system.partition('_')[-1])
        if size > max_size:
            continue
        candidates.append((size, system))
    return max(candidates, key=lambda val: val[0], default=['',''])[1]
