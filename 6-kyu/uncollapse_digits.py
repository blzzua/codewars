# https://www.codewars.com/kata/5a626fc7fd56cb63c300008c

import re

def uncollapse(digits):
    return ' '.join(re.findall('zero|one|two|three|four|five|six|seven|eight|nine', digits))

