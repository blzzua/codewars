# https://www.codewars.com/kata/58693136b98de0e4910001ab

from string import ascii_lowercase as al
def decrypt(test_key):
    return ''.join(str(test_key.count(letter)) for letter in al)

