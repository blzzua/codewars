# https://www.codewars.com/kata/56833b76371e86f8b6000015

import re

def to_cents(amount):
    m = re.match(r'^\$(\d+)\.(\d\d)\Z', amount)
    if m:
        print(amount)
        return int(m.expand(r'\1\2'))
