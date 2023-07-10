# https://www.codewars.com/kata/56d31aaefd3a52902a000d66

import re
def rad_ladies(name):
    return re.sub(r'[^A-Za-z\ \!]','',name).upper()
