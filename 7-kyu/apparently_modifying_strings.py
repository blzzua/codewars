# https://www.codewars.com/kata/5b049d57de4c7f6a6c0001d7

import re
def apparently(string):
    return re.sub(r'\b(and|but)\b(?! apparently\b)', r'\1 apparently', string)
