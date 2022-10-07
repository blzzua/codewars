# https://www.codewars.com/kata/552e45cc30b0dbd01100001a

def zipvalidate(postcode):
    return postcode.isdigit() and len(postcode) == 6 and not postcode[0] in ('0', '5', '7', '8', '9')

