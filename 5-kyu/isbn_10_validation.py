# https://www.codewars.com/kata/51fc12de24a9d8cb0e000001

import re
def valid_ISBN10(isbn):
    if not re.fullmatch(r'^\d{9}[0-9X]$', isbn):
        return False
    values_map = {'0': 0, '1': 1,'2': 2,'3': 3,'4': 4, '5': 5,'6': 6, '7': 7,'8': 8,'9': 9, 'X': 10}
    checksum = sum([values_map.get(x, -1000) * pos for pos, x in enumerate(isbn,1)])
    return checksum > 0 and checksum % 11 == 0
