# https://www.codewars.com/kata/575690ee34a34efb37001796

import re
def multiple_split(string, delimiters=[]):
    delimiters.append('empty delimiters list bug workaround by blzzua')
    return [p for p in re.split('|'.join([re.escape(d) for d in delimiters]), string) if p and p not in delimiters]
    

