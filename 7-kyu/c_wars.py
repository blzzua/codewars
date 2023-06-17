# https://www.codewars.com/kata/55968ab32cf633c3f8000008

def initials(name):
    name_parts = name.split(' ')
    return '.'.join([np[0].upper() for np in name_parts[:-1]] + [name_parts[-1].capitalize()] )
