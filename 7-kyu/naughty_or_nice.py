# https://www.codewars.com/kata/52a6b34e43c2484ac10000cd

def get_nice_names(people):
    return [p['name'] for p in people if p['was_nice']]
    
def get_naughty_names(people):
    return [p['name'] for p in people if not p['was_nice']]

