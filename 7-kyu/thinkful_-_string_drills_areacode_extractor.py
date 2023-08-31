# https://www.codewars.com/kata/585a36b445376cbc22000072

def area_code(text):
    return text.partition('(')[-1].partition(')')[0] # lazy
