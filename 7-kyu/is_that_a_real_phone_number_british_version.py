# https://www.codewars.com/kata/581a52d305fe7756720002eb

import re
def validate_number(string):
    if re.fullmatch(r'^(0|\+44)7\d{9}$', string.replace('-','')):
        return 'In with a chance'
    else:
        return 'Plenty more fish in the sea'
