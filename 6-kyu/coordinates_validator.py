# https://www.codewars.com/kata/5269452810342858ec000951

import re
def is_valid_coordinates(coordinates):
    m = re.fullmatch(r'^-?\d{1,2}(?:\.\d+)?, -?\d{1,3}(?:\.\d+)?$', coordinates)
    if m:
        lat, lon = [float(c) for c in m.string.split(', ')]
        if (-90 <= lat <= 90) and (-180 <= lon <= 180):
            return True
    return False

