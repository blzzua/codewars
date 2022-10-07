# https://www.codewars.com/kata/5cb05eee03c3ff002153d4ef

def get_section_id(scroll, sizes):
    tot = 0
    for i, h in enumerate(sizes):
        tot += h
        if tot > scroll:
            return i 
    return -1

