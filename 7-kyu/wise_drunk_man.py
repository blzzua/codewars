# https://www.codewars.com/kata/58e953ace87e856a97000046

import re
def wdm(talk):
    return re.sub('\s+',' ',re.sub('puke|hiccup','',talk)).strip()
