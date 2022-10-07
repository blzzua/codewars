# https://www.codewars.com/kata/6076d4edc7bf5d0041b31dcf

def sort_bytes(number):
    bytes = hex(2**32 + number)[3:]
    return int(''.join(sorted([h+l for h,l in zip(bytes[::2],bytes[1::2])],reverse=True)),16)

