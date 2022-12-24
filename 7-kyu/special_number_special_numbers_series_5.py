# https://www.codewars.com/kata/5a55f04be6be383a50000187

def special_number(number):
    return ['Special!!','NOT!!'][bool(set(str(number)) - set('012345'))]
