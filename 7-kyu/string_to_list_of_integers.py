# https://www.codewars.com/kata/5727868888095bdf5c001d3d

def string_to_int_list(s):    
    return [int(d) for d in s.split(',') if d.lstrip('-').isdigit()]

