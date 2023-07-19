# https://www.codewars.com/kata/56a24b309f3671608b00003a

import re

def dad_filter(string):
    return re.sub('([, ]+)?$','',re.sub(',+',',',string))
